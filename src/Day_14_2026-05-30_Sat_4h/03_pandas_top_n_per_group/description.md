# Pandas — Top N per Group

- **Difficulty**: Easy–Medium
- **Time budget**: ~20 min

## Objective
Practice groupby with filtering — one of the most common patterns in DS interviews.

## Task
Given a DataFrame with columns `employee_id`, `department`, and `salary`, return
the employees with the **highest salary in each department**.
If there is a tie, return **all tied employees**.
Sort the result by `department` ascending.

## Example
```
Input:
  employee_id  department   salary
  1            Engineering  90000
  2            Engineering  85000
  3            Engineering  90000
  4            Marketing    70000
  5            Marketing    65000

Output:
  employee_id  department   salary
  1            Engineering  90000
  3            Engineering  90000
  4            Marketing    70000
```

## Implement THREE ways
1. `groupby` + `transform('max')` — filter rows where salary equals group max
2. `groupby` + `rank(method='min', ascending=False)` — keep rank == 1
3. `sort_values` + `groupby` + `head(1)` — note: this does NOT handle ties correctly; explain why

## Self-check
- What does `transform` do differently from `agg`?
- Why does approach 3 fail for ties?
- What is the time complexity of each approach?
