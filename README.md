# Python Interview Prep — 2026-05-15

13-day study plan tailored for a .NET → Data Engineering / Data Science interview, targeting
2026-05-15.

## How to use this folder

Each day is a folder named `Day_NN_YYYY-MM-DD_Day_Hh`. Inside, exercises are numbered in the
recommended order. Each exercise has its own folder containing:

- `description.md` — read this first. Objective, data, task, expected output, hints, self-check.
- `data/*.csv` — sample data when relevant. Read it with pandas/PySpark in your solution.
- (you create) `solution.py`, `solution.sql`, `practice.py`, `notes.md`, etc.

### Recommended workflow per exercise

1. Open `description.md` in VS Code preview (Ctrl+Shift+V).
2. Set a timer based on the **Time budget** at the top.
3. Create a `solution.py` (or `.sql`) IN THE SAME FOLDER and code it without help.
4. Only check hints if stuck for >5 minutes.
5. Run, test edge cases, then read the **Self-check** section and answer it out loud.
6. Mark progress in `Python_Interview_Prep_Tracker.xlsx`.

## Daily plan summary

| Day | Date | Time | Focus | Exercises |
|-----|------|------|-------|-----------|
| 1   | Sat 5/2  | 4h | Python recap + warmup LC | 6 |
| 2   | Sun 5/3  | 4h | Algorithms core | 6 |
| 3   | Mon 5/4  | 1h | Strings + SQL kickoff | 4 |
| 4   | Tue 5/5  | 1h | Pandas I — DataFrame basics | 3 |
| 5   | Wed 5/6  | 1h | Pandas II — selecting & mutating | 3 |
| 6   | Thu 5/7  | 1h | Pandas III — missing data, reshape | 3 |
| 7   | Fri 5/8  | 2h | Pandas IV + PySpark intro | 4 |
| 8   | Sat 5/9  | 2h | SQL advanced (joins, windows) | 4 |
| 9   | Sun 5/10 | 2h | Algorithm review (all 8) | 8 |
| 10  | Mon 5/11 | 1h | OOP — design HashSet + concepts | 2 |
| 11  | Tue 5/12 | 1h | PySpark deep dive | 2 |
| 12  | Wed 5/13 | 1h | ETL design + data modeling | 2 |
| 13  | Thu 5/14 | 1h | Behavioral + mock + final review | 3 |
| —   | Fri 5/15 | —  | INTERVIEW DAY 🎯 | — |

## Setup

If you want to run pandas / PySpark locally:

```bash
python -m venv .venv
source .venv/bin/activate    # or .venv\Scripts\activate on Windows
pip install pandas pyspark
```

VS Code: install the Python and Jupyter extensions. Use the `.venv` interpreter.

## Companion files

- `Python_Interview_Prep_Plan.docx` — narrative plan
- `Python_Interview_Prep_Tracker.xlsx` — progress tracker
