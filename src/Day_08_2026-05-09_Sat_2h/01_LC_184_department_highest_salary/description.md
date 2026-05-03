# LC 184 — Department Highest Salary (SQL)

- **Source**: https://leetcode.com/problems/department-highest-salary/
- **Difficulty**: Medium
- **Time budget**: ~30 min

## Objective
`MAX` per group + JOIN. The classic 'top per group' pattern.

## Data
See `data/Employee.csv` and `data/Department.csv`.

## Task
Find employees who earn the highest salary in each department. Return `Department, Employee, Salary`.

Save TWO solutions in `solution.sql`:
1. Using a subquery `WHERE (departmentId, salary) IN (SELECT departmentId, MAX(salary) FROM Employee GROUP BY departmentId)`.
2. Using a window function: `RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC)`.

## Expected output
```
| Department | Employee | Salary |
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |  -- if there's a tie
| Sales      | Henry    | 80000  |
```

## Self-check
- What's the difference between `RANK`, `DENSE_RANK`, and `ROW_NUMBER` for ties?
- Which would you use here, and why?
