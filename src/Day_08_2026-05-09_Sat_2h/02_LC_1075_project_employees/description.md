# LC 1075 — Project Employees I (SQL)

- **Source**: https://leetcode.com/problems/project-employees-i/
- **Difficulty**: Easy
- **Time budget**: ~15 min

## Objective
GROUP BY + AVG + ROUND.

## Data
See `data/Project.csv` and `data/Employee.csv`.

## Task
Report `project_id` and the average years of experience of its employees, rounded to 2 decimals.

```sql
SELECT p.project_id, ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project p
JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id;
```

## Expected output
DataFrame with `project_id, average_years`.

## Self-check
What if an employee is on multiple projects? (Re-read the schema.)
