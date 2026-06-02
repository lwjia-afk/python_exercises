# ETL Pipeline — My Verbal Answer

**Scenario**: Daily pipeline — CSV files land in cloud storage, join with a Postgres/SQL reference table, write result to a data warehouse.

---

## 0. Platform Overview — AWS vs Azure vs GCP vs Hadoop

| Concept | AWS | Azure | GCP | Hadoop (on-prem) |
|---|---|---|---|---|
| File storage | S3 | ADLS Gen2 / Blob Storage | GCS | HDFS |
| Event trigger | SNS + SQS | Event Grid + Service Bus | Pub/Sub | Kafka |
| Orchestration | MWAA (managed Airflow) | Azure Data Factory (ADF) | Cloud Composer | Airflow (self-hosted) |
| Compute | EMR (Spark) | Synapse / HDInsight | Dataproc | YARN + Spark |
| Warehouse | Redshift | Synapse Analytics / Azure SQL | BigQuery | Hive |
| Managed Spark | Databricks (on AWS) | Databricks (on Azure) | Databricks (on GCP) | Spark on YARN |

In interviews: pick one stack to anchor your answer, then mention alternatives. I'll use **Azure** as the primary with AWS/GCP callouts.

---

## 1. Extract — how do I discover new files?

**Two approaches depending on latency needs:**

### Event-driven (low latency)
- **Azure**: CSV lands in ADLS Gen2 → **Azure Event Grid** fires an event → **Azure Service Bus** queues it → ADF pipeline or a Python Azure Function kicks off
- **AWS**: S3 → SNS → SQS → Lambda / Airflow sensor
- **GCP**: GCS → Pub/Sub → Cloud Function / Cloud Composer
- **Hadoop/on-prem**: Kafka topic receives file-arrival event → Spark Streaming or Airflow picks it up

### Scheduled scan (daily batch — my choice here)
- **Airflow DAG** (or **ADF trigger**) runs at 6am, scans the storage prefix for today's partition:
  - Azure: `abfss://container@account.dfs.core.windows.net/data/2026-05-13/*.csv`
  - AWS S3: `s3://bucket/data/2026-05-13/*.csv`
  - HDFS: `hdfs://namenode/data/2026-05-13/*.csv`

For a *daily* batch, scheduled scan is simpler and more predictable.

**Validation at extract (Python):**
```python
import pandas as pd
from azure.storage.filedatalake import DataLakeServiceClient

def validate_file(path: str) -> bool:
    df = pd.read_csv(path, nrows=1)
    expected_cols = {"id", "amount", "event_date"}
    if not expected_cols.issubset(df.columns):
        raise ValueError(f"Missing columns: {expected_cols - set(df.columns)}")
    return True
```

---

## 2. Transform — where does the join happen?

I use **PySpark** because CSV files in cloud storage can be large — Spark distributes the read and join across a cluster.

### PySpark on Azure (Synapse / Databricks / HDInsight)
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast, col, to_date, current_date

spark = SparkSession.builder.appName("daily_etl").getOrCreate()

# Read CSV from ADLS Gen2 (Azure) — change path for S3/GCS/HDFS
raw_df = spark.read.option("header", True).csv(
    "abfss://container@account.dfs.core.windows.net/data/2026-05-13/*.csv"
)

# Read reference table from Postgres (or Azure SQL / Synapse)
jdbc_url = "jdbc:postgresql://host:5432/mydb"
ref_df = spark.read.jdbc(jdbc_url, "reference_table", properties={
    "user": "user", "password": "password", "driver": "org.postgresql.Driver"
})

# Broadcast the small reference table — no shuffle, fast join
result_df = (
    raw_df
    .join(broadcast(ref_df), on="id", how="left")
    .withColumn("processing_date", current_date())
    .dropDuplicates(["id", "event_date"])
)

result_df.write.mode("overwrite").partitionBy("processing_date").parquet(
    "abfss://container@account.dfs.core.windows.net/output/"
)
```

### Why broadcast join?
- Reference table (Postgres) is small → replicated to every Spark worker
- No shuffle across the network → 5–10× faster than a regular join

### Pure Python alternative (small data — pandas)
```python
import pandas as pd
from sqlalchemy import create_engine

raw_df = pd.read_csv("data/2026-05-13.csv")
engine = create_engine("postgresql://user:password@host/mydb")
ref_df = pd.read_sql("SELECT * FROM reference_table", engine)

result_df = raw_df.merge(ref_df, on="id", how="left")
result_df["processing_date"] = pd.Timestamp.today().date()
result_df.drop_duplicates(subset=["id", "event_date"], inplace=True)
result_df.to_parquet("output/2026-05-13.parquet", index=False)
```
Use pandas when data fits in memory (<1GB). Use PySpark when it doesn't.

---

## 3. Load — full refresh vs incremental?

| Strategy | When to use | Risk |
|---|---|---|
| Full refresh | Small table (<10M rows), history doesn't matter | Slow, rewrites everything |
| Incremental (append) | Large table, partitioned by date | Risk of duplicates if not idempotent |
| Upsert (MERGE) | Records can be updated (not just inserted) | More complex SQL |

**My choice**: incremental load partitioned by `processing_date`. Safe rerun = delete partition, then insert.

```python
# Azure Synapse / PostgreSQL — safe idempotent load
import psycopg2

conn = psycopg2.connect("postgresql://user:password@host/mydb")
cur = conn.cursor()

processing_date = "2026-05-13"
cur.execute("DELETE FROM target_table WHERE processing_date = %s", (processing_date,))
cur.execute("""
    COPY target_table FROM 's3://bucket/output/2026-05-13.parquet'
    IAM_ROLE 'arn:aws:iam::...' FORMAT AS PARQUET
""")
conn.commit()
```

---

## 4. Orchestration — Airflow DAG

```
DAG: daily_etl  (schedule: 0 6 * * *)   ← runs at 6am every day

  [check_file_exists]          ← S3Sensor / AzureBlobSensor / GCSObjectSensor
        ↓
  [spark_extract_transform]    ← SparkSubmitOperator / DatabricksRunNow
        ↓
  [load_to_warehouse]          ← PostgresOperator / MsSqlOperator / BigQueryInsertJobOperator
        ↓
  [data_quality_check]         ← PythonOperator running assertions
        ↓
  [notify_success]             ← SlackWebhookOperator / EmailOperator
```

```python
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.providers.microsoft.azure.sensors.wasb import WasbBlobSensor
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
    "email_on_failure": True,
    "email": ["oncall@company.com"],
}

with DAG(
    "daily_etl",
    schedule_interval="0 6 * * *",
    start_date=datetime(2026, 1, 1),
    default_args=default_args,
    catchup=False,
) as dag:

    check_file = WasbBlobSensor(        # swap for S3KeySensor on AWS
        task_id="check_file_exists",
        container_name="container",
        blob_name="data/{{ ds }}/*.csv",
        timeout=3600,
    )

    transform = SparkSubmitOperator(
        task_id="spark_extract_transform",
        application="jobs/etl_transform.py",
        conn_id="spark_default",
        application_args=["--date", "{{ ds }}"],
    )

    load = PostgresOperator(
        task_id="load_to_warehouse",
        sql="sql/load_incremental.sql",
        postgres_conn_id="warehouse",
    )

    def quality_check(**ctx):
        # row count and null rate assertions
        pass

    check_quality = PythonOperator(
        task_id="data_quality_check",
        python_callable=quality_check,
    )

    check_file >> transform >> load >> check_quality
```

### Azure Data Factory alternative
ADF is Microsoft's GUI-based orchestrator — no Python needed. You build pipelines by dragging and dropping activities (Copy Data, Databricks Notebook, Stored Procedure). Good for teams that prefer low-code; Airflow is better when you need Python logic and version control.

---

## 5. Idempotency — safe reruns without double-counting

**Rule**: same input → same output, no matter how many times you run it.

```python
def idempotent_load(df: pd.DataFrame, processing_date: str, engine):
    with engine.begin() as conn:
        conn.execute(
            "DELETE FROM target_table WHERE processing_date = :d",
            {"d": processing_date}
        )
        df.to_sql("target_table", conn, if_exists="append", index=False)
```

- Delete the partition for that date, then insert fresh → rerunning never double-counts
- Airflow backfill: `airflow dags backfill -s 2026-05-06 -e 2026-05-13 daily_etl`

---

## 6. Monitoring — metrics and alerts

| What | How |
|---|---|
| Pipeline success/failure | Airflow alerts + Slack/Teams webhook |
| Row count vs yesterday | Assert: `today_rows > 0.8 × yesterday_rows` |
| Null rate on key columns | Assert: `null_rate < 1%` |
| Job duration | Alert if Spark job > 2× baseline |
| File arrival | Alert if no file by 5:30am (before 6am pipeline) |

```python
def data_quality_check(df: pd.DataFrame):
    assert len(df) > 0, "Empty result — pipeline produced no rows"
    null_rate = df["id"].isnull().mean()
    assert null_rate < 0.01, f"Null rate too high: {null_rate:.2%}"
```

Use **Great Expectations** for more structured checks; simple Python assertions for lightweight pipelines.

---

## 7. Failures — what if the CSV is malformed?

```python
import logging

def safe_extract(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path, dtype={"id": str, "amount": float})
    except Exception as e:
        logging.error(f"Failed to parse {path}: {e}")
        # Move to quarantine prefix in ADLS / S3
        move_to_quarantine(path)
        raise

    bad_rows = df[df["amount"].isnull()]
    if not bad_rows.empty:
        bad_rows.to_csv("error/quarantine.csv", index=False)  # don't drop silently
        df = df.dropna(subset=["amount"])

    return df
```

Layers of defense:
1. **Schema validation at extract** — fail fast, do NOT load bad data
2. **Row-level quarantine** — bad rows go to `error/` prefix for manual review
3. **Transactional load** — warehouse COPY inside a transaction; if it fails mid-way, it rolls back
4. **Airflow retry** — transient failures (network, throttle) retry automatically; after max retries, page on-call

---

## 8. Cost — bottleneck and optimization

**Bottleneck**: usually the Spark job (compute) or warehouse COPY (I/O).

| Optimization | Reason |
|---|---|
| Partition pruning | Filter by date so Spark only reads today's files, not all history |
| Parquet instead of CSV | Columnar format, 5–10× smaller, faster warehouse reads |
| Broadcast join | Small reference table replicated to workers — avoids shuffle |
| Right-size cluster | Spin up EMR/Synapse/Dataproc for the job, then terminate — don't run 24/7 |
| Compression (Snappy/gzip) | Reduces S3/ADLS storage cost and warehouse COPY time |
| Pandas for small data | Skip Spark overhead entirely when data fits in memory |

---

## 9. Tool Decision Tree

```
Data fits in memory (<1GB)?
    YES → pandas + Python (simple, fast, no cluster needed)
    NO  → PySpark on cloud cluster

Already in the warehouse?
    YES → dbt (SQL-first, version-controlled, no extra compute)
    NO  → Spark/Glue to ingest raw files first, then dbt inside the warehouse

Team prefers GUI / low-code?
    YES → Azure Data Factory or AWS Glue visual editor
    NO  → Airflow DAG in Python (version-controlled, flexible)

On-premise / no cloud?
    → HDFS + Spark on YARN + self-hosted Airflow
```

---

## Summary

| Step | Tool (Azure) | Tool (AWS) | Tool (GCP) | Tool (Hadoop) |
|---|---|---|---|---|
| Storage | ADLS Gen2 | S3 | GCS | HDFS |
| Event trigger | Event Grid | SNS/SQS | Pub/Sub | Kafka |
| Orchestration | ADF / Airflow | MWAA / Airflow | Cloud Composer | Airflow |
| Compute | Synapse / Databricks | EMR / Databricks | Dataproc | Spark on YARN |
| Warehouse | Synapse Analytics | Redshift | BigQuery | Hive |
| Transform (code) | PySpark / pandas | PySpark / pandas | PySpark / pandas | PySpark / pandas |
