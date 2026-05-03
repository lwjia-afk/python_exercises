# LC 2877 — Create a DataFrame from List

- **Source**: https://leetcode.com/problems/create-a-dataframe-from-list/
- **Difficulty**: Easy
- **Time budget**: ~15 min

## Objective
The most fundamental pandas operation. Build muscle memory.

## Data
A list of lists `student_data = [[1,15],[2,11],[3,11],[4,20]]` — id and age.

## Task
In `solution.py`, write a function `createDataframe(student_data)` that returns a pandas DataFrame with columns `student_id` and `age`.

```python
import pandas as pd

def createDataframe(student_data):
    # your code here
    pass
```

## Expected output
```
   student_id  age
0           1   15
1           2   11
2           3   11
3           4   20
```

## Self-check
What's the difference between `pd.DataFrame(data)` and `pd.DataFrame.from_records(data)`?
