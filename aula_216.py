import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
    .appName("Aula Introdut�ria PySpark") \
    .config("spark.executor.memory", "1gb") \
    .getOrCreate()

sc = spark.sparkContext

rdd = sc.textFile('World Population Datasets  - World Population 2023 by Country.csv')

rdd_new = rdd.map(lambda line: line.split(","))

#rdd_new.take(7)
rdd.take(5)
#rdd.first()