-- SQL — Median Salary per Department
-- Write your solution below.
-- Hint: use a CTE with ROW_NUMBER() and COUNT() OVER (PARTITION BY company),
--       then filter in the outer query.

-- Setup (run this first to create test data):
-- CREATE TABLE employee (id INT, company VARCHAR(10), salary INT);
-- INSERT INTO employee VALUES
-- (1,'A',2341),(2,'A',341),(3,'A',15),(4,'A',15314),(5,'A',451),(6,'A',513),
-- (7,'B',15),(8,'B',13000),(9,'B',1154),(10,'B',1345),
-- (11,'C',2345),(12,'C',2300);

WITH ranked AS (
    SELECT
        id,
        company,
        salary,
        -- TODO: add ROW_NUMBER() window function here
        -- TODO: add COUNT(*) window function here
    FROM employee
)
SELECT id, company, salary
FROM ranked
WHERE
    -- TODO: add median filter condition here
ORDER BY company, salary;
