# SQL window functions cheatsheet & drill

- **Time budget**: ~30 min

## Objective
Window functions are the #1 thing that distinguishes intermediate from beginner SQL. Drill them.

## Data
See `data/sales.csv` with `salesperson, region, sale_date, amount`.

## Task
In `solution.sql`, write queries for:

1. Rank salespeople within each region by total sales (use `RANK()`).
2. Running cumulative total per salesperson over time (use `SUM() OVER (PARTITION BY ... ORDER BY ...)`).
3. For each row, the previous sale's amount for the same salesperson (use `LAG()`).
4. Day-over-day percent change for each salesperson.
5. Top 2 salespeople per region (use a CTE wrapped around `RANK()`).

## Expected output
All five queries written, even if you can't run them locally — the muscle memory is the goal.

## Self-check
- When MUST you use a CTE / subquery to filter on a window function? (You can't put `RANK()` in a WHERE clause directly — why?)
- What's the difference between `PARTITION BY` and `GROUP BY`?
