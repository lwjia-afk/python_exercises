# Pandas groupby + aggregation

- **Time budget**: ~30 min

## Objective
`groupby` is the most asked-about pandas feature in interviews — get fluent.

## Data
See `data/sales.csv` with `region, product, quantity, price`.

## Task
In `solution.py`, compute:

1. Total `quantity` per `region`.
2. Average `price` per `product`.
3. Per `region`: total revenue (`quantity * price`) — add a derived column first.
4. Per `region` AND `product`: total quantity (multi-key groupby).
5. Top 2 products by revenue using `groupby` + `nlargest`.

## Expected output
All 5 outputs printed, with column names that read like a report.

## Hints
- `df.groupby('region')['quantity'].sum()`
- `.agg({'quantity':'sum','price':'mean'})` for multi-aggregation.
- `.reset_index()` if you want a flat DataFrame back.

## Self-check
What's the difference between `.agg()` and `.transform()`? When do you need each?
