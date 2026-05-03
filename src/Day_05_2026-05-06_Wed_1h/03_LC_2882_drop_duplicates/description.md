# LC 2882 — Drop Duplicate Rows

- **Source**: https://leetcode.com/problems/drop-duplicate-rows/
- **Difficulty**: Easy
- **Time budget**: ~15 min

## Objective
`drop_duplicates(subset=...)`.

## Data
See `data/customers.csv` with `customer_id, name, email`.

## Task
Drop duplicates based on `email`, keeping the FIRST occurrence.

## Expected output
DataFrame without duplicates.

## Hints
`df.drop_duplicates(subset=['email'], keep='first')`

## Self-check
What does `keep='last'` vs `keep=False` do?
