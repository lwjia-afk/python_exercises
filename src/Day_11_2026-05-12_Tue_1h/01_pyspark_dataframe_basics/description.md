# PySpark DataFrame basics

- **Time budget**: ~30 min

## Objective
Become comfortable with `select`, `filter`, `withColumn`, `groupBy`, `agg`, `orderBy`, `join`.

## Data
See `data/users.csv` and `data/events.csv`.

## Task
In `solution.py`:

```python
from pyspark.sql import SparkSession, functions as F
spark = SparkSession.builder.appName("basics").getOrCreate()

users = spark.read.csv("data/users.csv", header=True, inferSchema=True)
events = spark.read.csv("data/events.csv", header=True, inferSchema=True)
```

Implement:
1. Show users older than 30, sorted by age desc.
2. Add column `age_group` = 'young' if age<30 else 'adult' using `F.when`.
3. For each user, count events. (groupBy + count)
4. Join users + events. Then per `country`, total events.
5. Save the per-country result as parquet to `output/country_events`.

## Expected output
If installed, `.show()` outputs match a manual pandas calculation. If not installed, write the queries anyway and reason through them in NOTES.md.

## Self-check
- Why does `df.show()` trigger a job but `df.filter(...)` doesn't?
- What's the difference between `select`, `withColumn`, and `selectExpr`?
