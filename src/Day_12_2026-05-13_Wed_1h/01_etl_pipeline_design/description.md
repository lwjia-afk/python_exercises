# ETL pipeline design — verbal walk-through

- **Time budget**: ~40 min

## Objective
Be ready to whiteboard a small ETL pipeline. The interviewer wants to see:
- you decompose the problem (extract / transform / load)
- you mention error handling, idempotency, scheduling
- you name real tools (Airflow, dbt, Spark, S3, etc.)

## Task
Prepare a 5-minute verbal answer to: "Walk me through how you'd build a daily pipeline that ingests CSV files dropped in S3, joins them with a reference table in Postgres, and writes the result to a data warehouse."

Cover (write bullet points in `answer.md`):

1. **Extract**: how do you discover new files? (S3 event / scheduled scan)
2. **Transform**: where does the join happen? (Spark? dbt? trade-offs)
3. **Load**: full refresh vs incremental?
4. **Orchestration**: Airflow DAG structure, retries, alerts
5. **Idempotency**: how do you handle reruns without double-counting?
6. **Monitoring**: what metrics / alerts would you set up?
7. **Failures**: what happens if the source CSV is malformed?
8. **Cost**: what's the bottleneck? where would you optimize?

Practice saying it out loud — aim for ~5 minutes.

## Expected output
`answer.md` filled out with your version, then read it aloud once or twice.

## Self-check
If asked 'why dbt over Spark for the transform step?' — what's your answer? (No wrong answer, but have one ready.)
