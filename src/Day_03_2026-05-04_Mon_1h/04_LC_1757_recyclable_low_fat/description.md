# LC 1757 — Recyclable and Low Fat Products (SQL)

- **Source**: https://leetcode.com/problems/recyclable-and-low-fat-products/
- **Difficulty**: Easy
- **Time budget**: ~10 min

## Objective
Trivial WHERE clause warmup. Tests that you read the schema correctly.

## Data
See `data/Products.csv`. `Products(product_id, low_fats, recyclable)` where the latter two are 'Y'/'N'.

## Task
Write a query to find product_ids that are BOTH low fat AND recyclable. Save to `solution.sql`.

## Expected output
```sql
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
```

## Self-check
Could you express this with a CASE expression instead? Would you ever want to?
