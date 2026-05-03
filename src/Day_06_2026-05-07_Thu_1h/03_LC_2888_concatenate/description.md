# LC 2888 — Reshape Data: Concatenate

- **Source**: https://leetcode.com/problems/reshape-data-concatenate/
- **Difficulty**: Easy
- **Time budget**: ~15 min

## Objective
`pd.concat` for stacking DataFrames row-wise.

## Data
See `data/df1.csv` and `data/df2.csv` (same columns).

## Task
Concatenate them vertically.

## Expected output
A single DataFrame with all rows.

## Hints
`pd.concat([df1, df2], axis=0, ignore_index=True)`

## Self-check
What's `axis=0` vs `axis=1` in concat? When do you NEED `ignore_index=True`?
