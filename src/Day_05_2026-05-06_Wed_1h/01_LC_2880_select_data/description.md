# LC 2880 — Select Data

- **Source**: https://leetcode.com/problems/select-data/
- **Difficulty**: Easy
- **Time budget**: ~15 min

## Objective
Boolean indexing — the bread and butter of pandas.

## Data
See `data/students.csv` with columns `student_id, name, age`.

## Task
Select the row where `student_id == 101` and return only `[name, age]` columns.

## Expected output
A 1-row DataFrame.

## Hints
`df.loc[df['student_id'] == 101, ['name','age']]`

## Self-check
What does `df.loc` accept? How is it different from `df.iloc`?
