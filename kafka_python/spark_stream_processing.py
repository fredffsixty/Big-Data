from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import findspark

KAFKA_TOPIC_NAME_PROD = "titanic"
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
KAFKA_TOPIC_NAME_CONS = "survived"


if __name__ == '__main__':
    
    # Creiamo la SparkSession
    location = findspark.find()
    findspark.init(location)
    spark = SparkSession.builder.appName('SparkStreamingApp').getOrCreate()
    spark.sparkContext.setLogLevel('ERROR')
    
    # Leggiamo lo stream a partire dall'ultimo offset nel topic per effettuare una query streaming
    kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS) \
    .option("kafka.security.protocol", "PLAINTEXT") \
    .option("failOnDataLoss", "false") \
    .option("subscribe", KAFKA_TOPIC_NAME_PROD) \
    .option("includeHeaders", "false") \
    .option("startingOffsets", "latest") \
    .option("spark.streaming.kafka.maxRatePerPartition", "50") \
    .load()
    
    # creiamo il dataframe in ingresso effettuando il casting del
    # flusso di byte di ogni messaggio nella coppia di stringhe chiave-valore
    # che questo contiene
    kafka_df = kafka_df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
    
    # leggiamo i campi della stringa value e inseriamo apposite colonne
    split_col = split(kafka_df['value'],',')
    
    kafka_df = kafka_df.withColumn('Survived',split_col.getItem(0).cast('integer'))
    kafka_df = kafka_df.withColumn('Class',split_col.getItem(1).cast('integer'))
    # nel nostro data set la stringa del nome contiene carattere ','
    kafka_df = kafka_df.withColumn('Name',concat_ws(',',split_col.getItem(2),split_col.getItem(3)))  
    kafka_df = kafka_df.withColumn('Gender',split_col.getItem(4))
    kafka_df = kafka_df.withColumn('Age',split_col.getItem(5).cast('float'))
    
    # Selezioniamo i sopravvissuti per classe e genere
    kafka_df = kafka_df.filter("Survived == 1 AND Gender == 'female' AND Class == 1")
    
    # Selezioniamo le sole colonne che emetteremo in uscita
    female_survived_first_class = kafka_df['key','Name','Age']
    
    # Generiamo uno stream in uscita su un topic dedicato
    # in modo che un altro consumer possa leggerli
    out_df_stream_2 = female_survived_first_class \
        .selectExpr("CAST(key AS STRING)", "to_json(struct(Name,Age)) AS value") \
        .writeStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS) \
        .option("topic", KAFKA_TOPIC_NAME_CONS) \
        .trigger(processingTime='1 seconds') \
        .outputMode("update") \
        .option('checkpointLocation','/home/rpirrone/src/kafka_python/streaming_checkpoint') \
        .start() \
        .awaitTermination()
        
    print("SparkStreamingApp terminated")