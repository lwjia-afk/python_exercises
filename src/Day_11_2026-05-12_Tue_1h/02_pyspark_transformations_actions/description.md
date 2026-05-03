# PySpark transformations vs actions + UDFs

- **Time budget**: ~30 min

## Objective
Be able to articulate:
- transformation (lazy, returns a new DataFrame): `select`, `filter`, `withColumn`, `groupBy`, `join`
- action (triggers execution): `count`, `collect`, `show`, `write`, `take`
- when to use a UDF (vs built-in `pyspark.sql.functions`)

Interview red flag: writing a UDF when a built-in function would do — UDFs are slow because they break Spark's optimizer.

## Data
`data/users.csv` from previous exercise (or copy it).

## Task
In `notes.md`:

1. List 5 transformations and 5 actions you've used.
2. Explain in 2 sentences why Spark is lazy.
3. Write a Spark UDF that returns the first letter of `name`. Then rewrite it WITHOUT a UDF using `F.substring`.
4. Show how to inspect a query plan: `df.explain()`.

In `solution.py`, demonstrate items 3 and 4 with code.

## Expected output
Notes written + working comparison.

## Self-check
What's the cost of `collect()` on a 1B-row DataFrame? When is it appropriate?
