# LC 2881 — Create a New Column

- **Source**: https://leetcode.com/problems/create-a-new-column/
- **Difficulty**: Easy
- **Time budget**: ~15 min

## Objective
Vectorized arithmetic on columns.

## Data
See `data/employees.csv` with `name, salary`.

## Task
Add a new column `bonus` equal to `2 * salary` and return the result.

## Expected output
DataFrame with original cols + `bonus`.

## Hints
`df['bonus'] = df['salary'] * 2`. Avoid `.apply()` here — vectorized arithmetic is much faster.

## Self-check
When IS `.apply` necessary? (Hint: when the operation can't be vectorized.)
