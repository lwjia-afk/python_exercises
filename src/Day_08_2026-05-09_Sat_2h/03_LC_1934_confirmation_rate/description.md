# LC 1934 — Confirmation Rate (SQL)

- **Source**: https://leetcode.com/problems/confirmation-rate/
- **Difficulty**: Medium
- **Time budget**: ~30 min

## Objective
LEFT JOIN + conditional aggregation. Common interview shape.

## Data
See `data/Signups.csv` and `data/Confirmations.csv`.

## Task
For each user in `Signups`, compute their confirmation rate = `confirmed / total messages`. If a user has no messages, the rate should be `0.00`. Round to 2 decimals.

```sql
SELECT s.user_id,
       ROUND(AVG(CASE WHEN c.action = 'confirmed' THEN 1.0 ELSE 0 END), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id;
```

Note: `AVG(CASE WHEN ... THEN 1 ELSE 0 END)` is a common pattern for "rate of X" calculations. The `LEFT JOIN` ensures users with no messages still appear (and AVG over a single NULL returns NULL → wrap in `COALESCE` or rely on the `0.00` from no rows).

## Expected output
One row per signup user with their confirmation rate (0.00 to 1.00).

## Self-check
- Why LEFT JOIN, not INNER?
- What does `AVG` do when the group has only NULL values?
