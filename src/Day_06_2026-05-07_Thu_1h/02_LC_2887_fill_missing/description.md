# LC 2887 — Fill Missing Data

- **Source**: https://leetcode.com/problems/fill-missing-data/
- **Difficulty**: Easy
- **Time budget**: ~15 min

## Objective
`fillna()` — filling NaN with a constant or another column.

## Data
See `data/products.csv` (some `quantity` values are missing).

## Task
Fill missing `quantity` with `0`.

## Expected output
DataFrame with no NaN in `quantity`.

## Hints
`df.fillna({'quantity': 0})` or `df['quantity'] = df['quantity'].fillna(0)`

## Self-check
What's `ffill` vs `bfill`? When would you use each?
