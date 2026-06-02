"""
Pandas — 选择与过滤 (Selection & Filtering)
Difficulty: Easy
"""

import pandas as pd
import numpy as np


def make_df() -> pd.DataFrame:
    return pd.DataFrame({
        "name":       ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace"],
        "department": ["Engineering", "Marketing", "Engineering", "HR", "Marketing", "Engineering", "HR"],
        "age":        [28, 35, 24, 42, 31, 27, 38],
        "salary":     [95000, 72000, 88000, 55000, 68000, 91000, 52000],
        "years":      [3, 8, 2, 15, 6, 4, 12],
    }, index=["E001", "E002", "E003", "E004", "E005", "E006", "E007"])


# ── Task 1: loc vs iloc ──────────────────────────────────────────────────────

def select_rows_by_label(df: pd.DataFrame) -> pd.DataFrame:
    """用 loc 选 'E002' 到 'E004' 的行，只保留 name 和 salary 列"""
    return df.loc["E002" : "E004", ["name", "salary"]]


def select_rows_by_position(df: pd.DataFrame) -> pd.DataFrame:
    """用 iloc 选第 1~3 行（不含第 4），只保留第 0 和第 3 列"""
    return df.iloc[1:4, [0, 3]]
    


# ── Task 2: 布尔索引 ─────────────────────────────────────────────────────────

def high_salary_engineers(df: pd.DataFrame) -> pd.DataFrame:
    """salary > 80000 AND department == 'Engineering'"""
    return df.loc[(df["salary"] > 80000) & (df["department"] == "Engineering")]



def eng_or_marketing(df: pd.DataFrame) -> pd.DataFrame:
    """department 是 Engineering 或 Marketing（用 isin）"""
    return df.loc[df["department"].isin(["Engineering", "Marketing"])]


def non_hr(df: pd.DataFrame) -> pd.DataFrame:
    """department 不是 HR（用 ~ 取反 + isin）"""
    return df.loc[~df["department"].isin(["HR"])]


# ── Task 3: query ────────────────────────────────────────────────────────────

def query_high_salary_engineers(df: pd.DataFrame) -> pd.DataFrame:
    """用 query 重写 high_salary_engineers"""
    return df.query("salary > 80000 and department == 'Engineering'")


def query_with_external_var(df: pd.DataFrame, min_salary: int) -> pd.DataFrame:
    """
    用 query 过滤 salary >= min_salary，
    min_salary 是外部变量，用 @min_salary 引用
    """
    return df.query("salary >= @min_salary")



# ── Task 4: where / mask ─────────────────────────────────────────────────────

def apply_salary_floor(df: pd.DataFrame, floor: int = 60000) -> pd.DataFrame:
    """
    将 salary 列中低于 floor 的值替换为 floor。
    提示：用 where 或 clip，不要用 apply（太慢）。
    """
    df["salary"] = df["salary"].clip(lower=floor)
    return df


def mask_low_years(df: pd.DataFrame, min_years: int = 5) -> pd.DataFrame:
    """
    将 years < min_years 的 salary 值替换为 NaN（mask 方法）。
    含义：工龄不足的薪资不参与统计。
    """
    mask = df["years"] > min_years
    df["salary"] = df["salary"].where(mask, other=np.nan)
    return df


# ── Task 5: 复杂条件 ─────────────────────────────────────────────────────────

def age_between(df: pd.DataFrame, low: int, high: int) -> pd.DataFrame:
    """用 between 选 age 在 [low, high] 之间的行"""
    return df[df["age"].between(low, high)]


def names_starting_with(df: pd.DataFrame, prefix: str) -> pd.DataFrame:
    """用 str.startswith 过滤 name"""
    return df[df["name"].str.startswith(prefix)]

# ── Tests ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    df = make_df()

    # Task 1
    r1 = select_rows_by_label(df)
    assert list(r1.index) == ["E002", "E003", "E004"]
    assert list(r1.columns) == ["name", "salary"]
    print("select_rows_by_label ✓")

    r2 = select_rows_by_position(df)
    assert len(r2) == 3
    assert r2.columns.tolist() == ["name", "salary"]
    print("select_rows_by_position ✓")

    # Task 2
    r3 = high_salary_engineers(df)
    assert all(r3["salary"] > 80000)
    assert all(r3["department"] == "Engineering")
    print(f"high_salary_engineers ✓ → {r3['name'].tolist()}")

    r4 = eng_or_marketing(df)
    assert set(r4["department"].unique()) == {"Engineering", "Marketing"}
    print(f"eng_or_marketing ✓ → {len(r4)} rows")

    r5 = non_hr(df)
    assert "HR" not in r5["department"].values
    print(f"non_hr ✓ → {len(r5)} rows")

    # Task 3
    r6 = query_high_salary_engineers(df)
    assert r3.equals(r6), "query result should match boolean indexing"
    print("query_high_salary_engineers ✓")

    r7 = query_with_external_var(df, min_salary=80000)
    assert all(r7["salary"] >= 80000)
    print(f"query_with_external_var ✓ → {len(r7)} rows")

    # Task 4
    r8 = apply_salary_floor(df, floor=60000)
    assert r8["salary"].min() >= 60000
    print(f"apply_salary_floor ✓ → min salary {r8['salary'].min()}")

    r9 = mask_low_years(df, min_years=5)
    low_years_count = (df["years"] < 5).sum()
    assert r9["salary"].isna().sum() == low_years_count
    print(f"mask_low_years ✓ → {r9['salary'].isna().sum()} masked")

    # Task 5
    r10 = age_between(df, 25, 35)
    assert r10["age"].between(25, 35).all()
    print(f"age_between ✓ → {r10['name'].tolist()}")

    r11 = names_starting_with(df, "E")
    assert all(r11["name"].str.startswith("E"))
    print(f"names_starting_with('E') ✓ → {r11['name'].tolist()}")

    print("\n✅ All tests passed!")
