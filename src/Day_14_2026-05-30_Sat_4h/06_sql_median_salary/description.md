# SQL — Median Salary per Department

- **Source**: LC 569 (Premium) — Median Employee Salary
- **Difficulty**: Medium–Hard
- **Time budget**: ~30 min

## Objective
Practice window functions for positional problems. Median is a classic interview question
that cannot be solved with just `AVG()`.

## Task
Given a table `employee`, find the employees whose salary is the **median** salary
for their company. If a company has an even number of employees, return **both middle records**.
Return all columns: `id`, `company`, `salary`. Order by `company`, then `salary`.

## Table Schema
```sql
CREATE TABLE employee (
    id      INT,
    company VARCHAR(10),
    salary  INT
);
```

## Sample Data
```sql
INSERT INTO employee VALUES
(1, 'A', 2341), (2, 'A', 341),  (3, 'A', 15),
(4, 'A', 15314),(5, 'A', 451),  (6, 'A', 513),
(7, 'B', 15),   (8, 'B', 13000),(9, 'B', 1154),
(10,'B', 1345), (11,'C', 2345), (12,'C', 2300);
```

## Expected Output
```
id  company  salary
5   A        451
6   A        513
9   B        1154
10  B        1345
11  C        2345
12  C        2300
```

## Approach
Use two window functions together:
- `ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary)` → row position (1-based)
- `COUNT(*) OVER (PARTITION BY company)` → total count in that company

A row is a median when its row number falls within the middle range:
```
row_num >= total_count / 2.0
AND
row_num <= total_count / 2.0 + 1
```

## Self-check
- Why doesn't `AVG(salary)` work here?
- What happens for a company with 1 employee? Does your query still return that row?
- What is the difference between `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()`?
  Which one is correct to use here and why?
