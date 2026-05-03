# Pandas merge / join

- **Time budget**: ~30 min

## Objective
`merge` is pandas's SQL JOIN. Cover inner / left / right / outer in one session.

## Data
See `data/orders.csv` and `data/customers.csv`.

## Task
In `solution.py`:

1. INNER join orders with customers on `customer_id`.
2. LEFT join: keep all orders, even those without a matching customer record. Identify any orphan orders.
3. Find customers with NO orders (anti-join via `merge` + `indicator=True`, then filter `_merge == 'left_only'`).
4. Add a `country_total_revenue` column to the orders DataFrame using a groupby + merge.

## Expected output
All four results printed.

## Hints
- `pd.merge(left, right, on='customer_id', how='inner')`
- `how='outer'` and `indicator=True` give you a column showing which side each row came from.

## Self-check
What's the pandas equivalent of SQL `LEFT JOIN ... WHERE r.id IS NULL`?
