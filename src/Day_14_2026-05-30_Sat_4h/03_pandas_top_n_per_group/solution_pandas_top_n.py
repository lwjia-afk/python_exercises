"""
Pandas — Top N per Group
Difficulty: Easy–Medium
"""

import pandas as pd


def make_df() -> pd.DataFrame:
    return pd.DataFrame({
        "employee_id": [1, 2, 3, 4, 5],
        "department":  ["Engineering", "Engineering", "Engineering", "Marketing", "Marketing"],
        "salary":      [90000, 85000, 90000, 70000, 65000],
    })


# ── Approach 1: groupby + transform ────────────────────────────────────────
# TODO: filter rows where salary == max salary of their department
def top_salary_transform(df: pd.DataFrame) -> pd.DataFrame:
    pass


# ── Approach 2: groupby + rank ──────────────────────────────────────────────
# TODO: use rank(method='min', ascending=False), keep rank == 1
def top_salary_rank(df: pd.DataFrame) -> pd.DataFrame:
    pass


# ── Approach 3: sort + head (intentionally broken for ties) ─────────────────
# TODO: implement, then explain in a comment why this does NOT handle ties
def top_salary_head(df: pd.DataFrame) -> pd.DataFrame:
    pass


# ── Tests ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    df = make_df()
    expected_ids = {1, 3, 4}

    for fn in [top_salary_transform, top_salary_rank]:
        result = fn(df)
        assert set(result["employee_id"]) == expected_ids, f"{fn.__name__} failed: {result}"
        print(f"{fn.__name__} ✓")
        print(result.sort_values("department").to_string(index=False))
        print()
