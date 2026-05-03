# LC 183 — Customers Who Never Order (SQL)

- **Source**: https://leetcode.com/problems/customers-who-never-order/
- **Difficulty**: Easy
- **Time budget**: ~15 min

## Objective
`NOT IN` / `LEFT JOIN ... IS NULL` / `NOT EXISTS` — three ways to express the same anti-join.

## Data
See `data/Customers.csv` and `data/Orders.csv`.

`Customers(id, name)`
`Orders(id, customerId)`

## Task
Find all customers who never placed an order.

Implement THREE versions in `solution.sql`:
1. `LEFT JOIN ... WHERE Orders.id IS NULL`
2. `WHERE id NOT IN (SELECT customerId FROM Orders)`
3. `WHERE NOT EXISTS (SELECT 1 FROM Orders WHERE Orders.customerId = Customers.id)`

In a comment, note the gotcha with `NOT IN` and NULLs.

## Expected output
```sql
-- Approach 1
SELECT name AS Customers
FROM Customers c
LEFT JOIN Orders o ON c.id = o.customerId
WHERE o.id IS NULL;
```

(plus the other two)

## Self-check
Why does `NOT IN` give wrong results if the subquery returns any NULL?
