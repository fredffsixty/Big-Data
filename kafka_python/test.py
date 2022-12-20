from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import findspark
from pyspark.accumulators import AccumulatorParam

# Creiamo la SparkSession
location = findspark.find()
findspark.init(location)
spark = SparkSession.builder.appName('SparkBatchApp').getOrCreate()
sc = spark.sparkContext
sc.setLogLevel('ERROR')

class VectorAccumulatorParam(AccumulatorParam):
    def zero(self, value):
        return [0.0] * len(value)
    def addInPlace(self, val1, val2):
        for i in range(len(val1)):
             val1[i] += val2[i]
        return val1

passengers_acc = sc.accumulator([0.0, 0.0, 0.0,\
                                 0.0, 0.0, 0.0,\
                                 0.0, 0.0, 0.0,\
                                 0.0, 0.0, 0.0,\
                                 0.0, 0.0, 0.0,\
                                 0.0, 0.0, 0.0], VectorAccumulatorParam())


def update_passengers(row):
    global passengers_acc
    
    passengers_acc += [\
    1.0 if row[2] == 1 and row[4] == 'female' else 0.0,\
    row[1] if row[2] == 1 and row[4] == 'female' else 0.0,\
    row[5] if row[5] != None and row[2] == 1 and row[4] == 'female' else 0.0,\
    1.0 if row[2] == 1 and row[4] == 'male' else 0.0,\
    row[1] if row[2] == 1 and row[4] == 'male' else 0.0,\
    row[5] if row[5] != None and row[2] == 1 and row[4] == 'male' else 0.0,\
    1.0 if row[2] == 2 and row[4] == 'female' else 0.0,\
    row[1] if row[2] == 2 and row[4] == 'female' else 0.0,\
    row[5] if row[5] != None and row[2] == 2 and row[4] == 'female' else 0.0,\
    1.0 if row[2] == 2 and row[4] == 'male' else 0.0,\
    row[1] if row[2] == 2 and row[4] == 'male' else 0.0,\
    row[5] if row[5] != None and row[2] == 2 and row[4] == 'male' else 0.0,\
    1.0 if row[2] == 3 and row[4] == 'female' else 0.0,\
    row[1] if row[2] == 3 and row[4] == 'female' else 0.0,\
    row[5] if row[5] != None and row[2] == 3 and row[4] == 'female' else 0.0,\
    1.0 if row[2] == 3 and row[4] == 'male' else 0.0,\
    row[1] if row[2] == 3 and row[4] == 'male' else 0.0,\
    row[5] if row[5] != None and row[2] == 3 and row[4] == 'male' else 0.0\
    ]


if __name__ == '__main__':
    
    
    # Importazione dei dati dal data set titanic.csv

    # costruzione dello schema del DataFrame

    passengerSchema = StructType([
        StructField('PassengerID',ShortType(),False),
        StructField('Survived',ShortType(),False),
        StructField('Pclass',ShortType(),False),
        StructField('Name',StringType(),False),
        StructField('Sex',StringType(),False),
        StructField('Age',FloatType(),True),
        StructField('SibSp',IntegerType(),True),
        StructField('Parch',IntegerType(),True),
        StructField('Ticket',StringType(),True),
        StructField('Fare',FloatType(),True),
        StructField('Cabin',StringType(),True),
        StructField('Embarked',StringType(),True)
    ])

    titanic = spark.read.format('csv')\
        .option('header','true')\
        .option('mode','FAILFAST')\
        .schema(passengerSchema)\
        .load('hdfs://localhost:9099/user/pirrone/spark/input/titanic.csv')
        
    
    titanic.rdd.foreach(update_passengers)

    
    