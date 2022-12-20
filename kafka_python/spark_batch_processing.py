from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.accumulators import AccumulatorParam

import findspark

KAFKA_TOPIC_NAME_PROD = "titanic"
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
KAFKA_TOPIC_NAME_CONS = "survived"


if __name__ == '__main__':
    
    # Creiamo la SparkSession
    location = findspark.find()
    findspark.init(location)
    spark = SparkSession.builder.appName('SparkBatchApp').getOrCreate()
    sc = spark.sparkContext
    sc.setLogLevel('ERROR')

    # Leggiamo tutto lo stream prodotto nel topic per effettuare una query batch
    kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS) \
    .option("kafka.security.protocol", "PLAINTEXT") \
    .option("failOnDataLoss", "false") \
    .option("startingOffsets", "earliest") \
    .option("subscribe", KAFKA_TOPIC_NAME_PROD) \
    .load()
    
    # creiamo il dataframe in ingresso effettuando il casting del
    # flusso di byte di ogni messaggio nella coppia di stringhe chiave-valore
    # che questo contiene
    kafka_df = kafka_df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
    kafka_df.dropDuplicates(['key'])
    
    # leggiamo i campi della stringa value e inseriamo apposite colonne
    split_col = split(kafka_df['value'],',')
    
    kafka_df = kafka_df.withColumn('Survived',split_col.getItem(0).cast('integer'))
    kafka_df = kafka_df.withColumn('Class',split_col.getItem(1).cast('integer'))
    # nel nostro data set la stringa del nome contiene il carattere ','
    kafka_df = kafka_df.withColumn('Name',concat_ws(',',split_col.getItem(2),split_col.getItem(3)))  
    kafka_df = kafka_df.withColumn('Gender',split_col.getItem(4))
    kafka_df = kafka_df.withColumn('Age',split_col.getItem(5).cast('float'))
    kafka_df = kafka_df.select('Survived','Class','Gender','Age').where('Survived==1')
    kafka_df = kafka_df.dropna()

    # Creiamo una query streaming in uscita che salva i risultati su un file in
    # formato Apache Parquet che è un formato comodo perché conserva lo schema
    query= kafka_df.writeStream\
        .option("checkpointLocation",'/home/rpirrone/src/kafka_python/batch_checkpoint')\
        .option('path','/home/rpirrone/src/kafka_python/save_stream')\
        .trigger(processingTime="5 seconds")\
        .format("parquet")\
        .start()

    query.awaitTermination(100)
    
    titanic = spark.read.format('parquet')\
        .load('/home/rpirrone/src/kafka_python/save_stream')
    
    titanic.groupBy('Gender','Class')\
                        .agg(expr('avg(Age) as avg_age'),expr('count(*) as surv_num'))\
                        .show()
    
    # Analogo risultato si poteva ottenere fintrando il df in ingresso e
    # salvandolo su una tabella sulla quale si esegue spark.sql()
    
    #survived = kafka_df.filter('Survived == 1').\
    #                    groupBy('Gender','Class').\
    #                    agg(expr('avg(Age) as avg_age'),expr('count(*) as surv_num'))
    #        
    #
    #survived.writeStream \
    #    .queryName("aggregates") \
    #    .outputMode("complete") \
    #    .format("memory") \
    #    .start().awaitTermination(100)

    #spark.sql("select * from aggregates").show()
    
    # Versione per debug su console
    
    #survived \
    #    .writeStream \
    #    .outputMode("complete") \
    #    .format("console")\
    #    .trigger(processingTime="5 seconds")\
    #    .start().awaitTermination(180)
    
    
    print("SparkBatchApp terminated")