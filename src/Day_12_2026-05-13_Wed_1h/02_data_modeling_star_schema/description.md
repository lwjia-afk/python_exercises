# Data modeling basics — star schema

- **Time budget**: ~20 min

## Objective
You'll likely get a 'design a schema' question. Star schema is the default answer for analytics workloads.

## Task
Scenario: A bookstore wants to analyze sales. Sources: orders (one row per item sold), customers, books, time.

In `schema.md`:

1. Identify the FACT table. What's its grain?
2. Identify dimension tables (at least 3).
3. Sketch the schema as a markdown table or ASCII diagram.
4. Write the SQL `CREATE TABLE` for the fact table.
5. Write a SQL query: top 5 books by revenue last quarter.

Touch on:
- surrogate vs natural keys
- slowly changing dimensions (Type 1 vs Type 2)
- when star schema is wrong (graph data, very high cardinality, real-time)

## Expected output
`schema.md` complete + you can sketch the diagram on paper without notes.

## Self-check
What's the difference between a star and a snowflake schema? When would you snowflake?
