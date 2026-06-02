"""
Pandas — GroupBy 与聚合 (GroupBy & Aggregation)
Difficulty: Medium
"""

import pandas as pd
import numpy as np


def make_df() -> pd.DataFrame:
    return pd.DataFrame({
        "name":       ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace", "Hank", "Iris"],
        "department": ["Eng", "Eng", "Eng", "Marketing", "Marketing", "HR", "HR", "HR", "Eng"],
        "level":      ["Senior", "Junior", "Senior", "Senior", "Junior", "Junior", "Senior", "Junior", "Junior"],
        "salary":     [95000, 72000, 88000, 78000, 65000, 55000, 62000, 51000, 69000],
        "bonus":      [10000, 5000, 9000, 8000, 4000, 3000, 5000, 2000, 6000],
    })


# ── Task 1: 基础聚合 ─────────────────────────────────────────────────────────

def dept_salary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    按 department 分组，返回：
    - avg_salary: salary 均值
    - max_salary: salary 最大值
    - headcount: 人数
    用 named aggregation 语法
    """
    new_df = df.groupby("department").agg(
        avg_salary=("salary", "mean"),
        max_salary=("salary", "max"),
        headcount=("name", "count")
    ).reset_index()
    return new_df



# ── Task 2: 多列分组 ─────────────────────────────────────────────────────────

def dept_level_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    按 department + level 分组，返回：
    - avg_salary: salary 均值
    - total_bonus: bonus 总和
    - headcount: name 计数
    打平索引（reset_index）
    """
    new_df = df.groupby(["department", "level"]).agg(
        avg_salary=("salary", "mean"),
        total_bonus=("bonus", "sum"),
        headcount=("name", "count")
    ).reset_index()
    return new_df

# ── Task 3: transform ────────────────────────────────────────────────────────

def add_salary_ratio(df: pd.DataFrame) -> pd.DataFrame:
    """
    新增两列（不修改原 df，返回新 df）：
    - salary_ratio: 该员工薪资 / 本部门薪资总和
    - salary_vs_dept_mean: 该员工薪资 - 本部门薪资均值
    """
    # TODO: 用 transform
    new_df = df.copy()
    new_df["salary_ratio"] = new_df["salary"] / new_df.groupby("department")["salary"].transform("sum")
    new_df["salary_vs_dept_mean"] = new_df["salary"] - new_df.groupby("department")["salary"].transform("mean")
    return new_df


# ── Task 4: filter ───────────────────────────────────────────────────────────

def high_avg_salary_depts(df: pd.DataFrame, threshold: int = 75000) -> pd.DataFrame:
    """保留部门平均薪资 > threshold 的所有员工行"""
    # TODO: groupby + filter
    new_df = df.groupby("department").filter(lambda g: g["salary"].mean() > threshold)
    return new_df


def large_depts(df: pd.DataFrame, min_headcount: int = 3) -> pd.DataFrame:
    """保留员工人数 >= min_headcount 的部门的所有行"""
    # TODO
    new_df = df.groupby("department").filter(lambda g: g["name"].count() >= min_headcount)
    return new_df


# ── Task 5: apply ────────────────────────────────────────────────────────────

def dept_min_max_employees(df: pd.DataFrame) -> pd.DataFrame:
    """
    对每个部门，返回薪资最高和最低的员工信息。
    期望输出格式（示例）：
      department  name   salary  type
      Eng         Alice  95000   max
      Eng         Iris   69000   min
      ...
    """
    df_max = df.loc[df.groupby("department")["salary"].idxmax()].assign(type="max")
    df_min = df.loc[df.groupby("department")["salary"].idxmin()].assign(type="min")
    new_df = pd.concat([df_max, df_min], ignore_index=True)
    return new_df[["department", "name", "salary", "type"]]
    

def dept_salary_quantiles(df: pd.DataFrame) -> pd.DataFrame:
    """
    计算每个部门薪资的 25%, 50%, 75% 分位数。
    返回 DataFrame，index 是 department，列是 q25, q50, q75。
    """
    return df.groupby("department")["salary"].quantile([0.25, 0.5, 0.75]).unstack(level=1).rename(columns={0.25: "q25", 0.5: "q50", 0.75: "q75"})


# ── Tests ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    df = make_df()

    # Task 1
    stats = dept_salary_stats(df)
    print("=== 部门薪资统计 ===")
    print(stats)
    assert "avg_salary" in stats.columns
    assert "headcount" in stats.columns
    assert stats.loc[stats["department"] == "Eng", "headcount"].values[0] == 4

    # Task 2
    dl_stats = dept_level_stats(df)
    print("\n=== 部门+级别统计 ===")
    print(dl_stats)
    assert "total_bonus" in dl_stats.columns
    assert len(dl_stats) > 0

    # Task 3
    df2 = add_salary_ratio(df)
    print("\n=== 薪资比例 ===")
    print(df2[["name", "department", "salary", "salary_ratio", "salary_vs_dept_mean"]])
    assert abs(df2.groupby("department")["salary_ratio"].sum().sub(1).max()) < 1e-9

    # Task 4
    high_dept = high_avg_salary_depts(df, threshold=75000)
    print(f"\n高均薪部门员工: {high_dept['name'].tolist()}")
    # Eng avg ≈ 81000 > 75000, Marketing avg ≈ 71500 < 75000
    assert "Marketing" not in high_dept["department"].values

    large = large_depts(df, min_headcount=3)
    print(f"大部门员工: {large['department'].unique()}")
    assert "HR" in large["department"].values  # HR 有 3 人

    # Task 5
    minmax = dept_min_max_employees(df)
    print("\n=== 各部门最高/最低薪资员工 ===")
    print(minmax)

    quantiles = dept_salary_quantiles(df)
    print("\n=== 薪资分位数 ===")
    print(quantiles)
    assert "q50" in quantiles.columns

    print("\n✅ All tests passed!")
