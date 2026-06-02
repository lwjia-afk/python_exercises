from pyspark.sql import functions as F
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType


spark = SparkSession.builder \
    .appName("pyspark02") \
    .config("spark.python.worker.faulthandler.enabled", "true") \
    .getOrCreate()


def get_firstletter(name):
    return name[0]

get_first_letter_udf = F.udf(get_firstletter, StringType())

df = spark.createDataFrame([("Alice",), ("Bob",), ("Charlie",)], ["name"])

df_with_first_letter = df.withColumn("first_letter", get_first_letter_udf(F.col("name")))

df_with_first_letter.show()
spark.stop()
