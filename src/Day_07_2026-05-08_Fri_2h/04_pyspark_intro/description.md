# PySpark intro — the 30-minute version

- **Time budget**: ~30 min

## Objective
Get the conceptual map. The interview won't expect you to be a Spark expert, but you SHOULD be able to:
- explain what a Spark DataFrame is vs a pandas DataFrame
- read CSV, do a filter / select / groupBy / agg, and write output
- explain lazy evaluation and the action vs transformation distinction

## Data
See `data/transactions.csv`.

## Task
Setup (skip if you can't install PySpark — read the docs instead):
```bash
pip install pyspark
```

In `solution.py`:
```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("intro").getOrCreate()
df = spark.read.csv("data/transactions.csv", header=True, inferSchema=True)

# 1. show schema
df.printSchema()

# 2. filter, then aggregate
result = (
    df.filter(F.col("amount") > 0)
      .groupBy("category")
      .agg(F.sum("amount").alias("total"))
      .orderBy(F.desc("total"))
)

result.show()
```

Read & note (if no install): https://spark.apache.org/docs/latest/sql-getting-started.html

## Expected output
If installed, you see the per-category totals printed. Otherwise, write a NOTES.md with key concepts you learned.

## Self-check
- What's a "transformation" vs an "action" in Spark?
- Why is Spark lazy?
- When would you choose Spark over pandas?
