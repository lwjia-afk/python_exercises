import os
from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("basics").getOrCreate()

data_dir = os.path.join(os.path.dirname(__file__), "data")
users = spark.read.csv(f"{data_dir}/users.csv", header=True, inferSchema=True)
events = spark.read.csv(f"{data_dir}/events.csv", header=True, inferSchema=True)

users.filter(users.age>30).show()

users = users.withColumn("age_group", F.when(users.age < 30, "young").otherwise("adult"))
users.show()

user_event = users.join(events, on="user_id", how="inner")
user_event_count = user_event.groupBy("user_id", "name").agg(F.count("*").alias("event_count"))
user_event_count.show()

country_event = user_event.groupBy("country").agg(F.count("*").alias("event_count"))
country_event.show()

os.makedirs(os.path.join(data_dir, "output"), exist_ok=True)
country_event.toPandas().to_csv(os.path.join(data_dir, "output", "country_event_count.csv"), index=False)
