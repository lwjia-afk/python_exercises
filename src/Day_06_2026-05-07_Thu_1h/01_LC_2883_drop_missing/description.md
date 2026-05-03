# LC 2883 — Drop Missing Data

- **Source**: https://leetcode.com/problems/drop-missing-data/
- **Difficulty**: Easy
- **Time budget**: ~15 min

## Objective
`dropna(subset=...)`.

## Data
See `data/students.csv` (some `name` values are missing).

## Task
Drop any row where `name` is missing.

## Expected output
DataFrame with no NaN in `name`.

## Hints
`df.dropna(subset=['name'])`

## Self-check
What does `df.dropna(how='all')` do vs `how='any'`?
