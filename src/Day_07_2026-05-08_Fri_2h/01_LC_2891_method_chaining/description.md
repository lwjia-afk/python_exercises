# LC 2891 — Method Chaining

- **Source**: https://leetcode.com/problems/method-chaining/
- **Difficulty**: Easy
- **Time budget**: ~20 min

## Objective
Practice the chained / pipeline style — important for clean pandas code.

## Data
See `data/animals.csv` with `name, species, age, weight`.

## Task
Find the names of animals that weigh strictly more than 100kg, sorted by weight in descending order.

Do it in ONE chain — no intermediate variables:
```python
result = (
    animals
    .loc[animals['weight'] > 100]
    .sort_values('weight', ascending=False)
    [['name']]
)
```

## Expected output
A DataFrame of `name` values, ordered by weight desc.

## Self-check
Why is method chaining nice for readability? What's the downside when debugging?
