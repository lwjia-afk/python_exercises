# LC 175 — Combine Two Tables (SQL)

- **Source**: https://leetcode.com/problems/combine-two-tables/
- **Difficulty**: Easy
- **Time budget**: ~15 min

## Objective
LEFT JOIN basics. The single most common SQL operation in data interviews.

## Data
See `data/Person.csv` and `data/Address.csv`.

`Person(personId, lastName, firstName)`
`Address(addressId, personId, city, state)`

## Task
Write a SQL query for a report containing `firstName, lastName, city, state` of EVERY person. If no address exists for a person, the city/state fields should be NULL.

Save the query as `solution.sql`.

If you want to validate locally, also write `verify.py` that loads the CSVs into pandas and reproduces the result with a `merge(how='left')` — useful for confirming the answer.

## Expected output
SQL query that returns one row per person, with NULL city/state when no address exists.

```sql
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId;
```

## Self-check
Why LEFT JOIN, not INNER JOIN? What would you get with INNER?
