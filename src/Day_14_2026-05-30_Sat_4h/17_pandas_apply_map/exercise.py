"""
Pandas — Apply / Map / Transform
Difficulty: Medium
"""

import pandas as pd
import numpy as np


def make_df() -> pd.DataFrame:
    return pd.DataFrame({
        "name":       ["Alice", "Bob", "Charlie", "Dave", "Eve"],
        "department": ["Engineering", "Marketing", "Engineering", "HR", "Marketing"],
        "salary":     [95000, 72000, 88000, 55000, 68000],
        "bonus":      [10000, 5000, 9000, 3000, 4000],
        "years":      [3, 8, 2, 15, 6],
    })


# ── Task 1: Series.map ───────────────────────────────────────────────────────

DEPT_MAP = {
    "Engineering": "工程部",
    "Marketing":   "市场部",
    "HR":          "人力资源部",
}


def translate_department_dict(df: pd.DataFrame) -> pd.Series:
    """用字典 map 翻译部门名，未匹配项保持为 NaN"""
    df["department_translated"] = df["department"].map(DEPT_MAP, na_action=None)  # na_action='ignore' 保持 NaN 不变
    return df["department_translated"]


def translate_department_func(df: pd.DataFrame) -> pd.Series:
    """用函数 map 翻译部门名，未匹配项保持原值"""
    return df["department"].map(lambda x: DEPT_MAP.get(x, x))  # type: ignore # get 方法未找到时返回 None，保持原值需要自定义函数


# ── Task 2: Series.apply（薪资等级）────────────────────────────────────────

def salary_level_apply(df: pd.DataFrame) -> pd.Series:
    """
    用 apply 给薪资分级：
    < 60000  → '低'
    60000~90000 → '中'
    > 90000  → '高'
    """
    def salary_level (x):
        if x < 60000 :
            return "低"
        elif x < 90000:
            return "中"
        else:
            return "高"
        
    new_df = df["salary"].apply(salary_level)
    return new_df


def salary_level_cut(df: pd.DataFrame) -> pd.Series:
    """
    用 pd.cut 实现相同效果（更快）。
    注意 right=True/False 对边界的影响。
    """
    # TODO: pd.cut(df['salary'], bins=[0, 60000, 90000, float('inf')], labels=['低','中','高'])
    new_df = pd.cut(df["salary"], bins = [0, 60000, 90000, float("inf")], labels= ["低","中","高"], right=True)
    return new_df


# ── Task 3: DataFrame.apply ──────────────────────────────────────────────────

def total_compensation(df: pd.DataFrame) -> pd.Series:
    """按行 apply：返回每个员工的 salary + bonus"""
    # TODO: axis=1（但其实直接向量化更好，练习 apply 语法即可）
    return df.apply(lambda row: row["salary"] + row["bonus"], axis=1)


def column_range_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    按列 apply：对每个数值列计算 min, max, range（max-min）。
    返回 DataFrame，行 index = ['min', 'max', 'range']，列 = 数值列名
    """
    # TODO: axis=0，自定义函数返回 pd.Series
    df_num = df.select_dtypes(include="number").apply(lambda col: pd.Series({
        "min": col.min(),
        "max": col.max(),
        "range": col.max() - col.min()
    }), axis=0)
    return df_num


# ── Task 4: DataFrame.map（元素级）──────────────────────────────────────────

def format_numbers(df: pd.DataFrame) -> pd.DataFrame:
    """
    对数值列（salary, bonus, years）格式化为带千位分隔符的字符串。
    95000 → '95,000'
    提示：f"{x:,}" 或 format(x, ',')
    """
    # TODO: df[cols].map(lambda x: ...)
    return df[["salary", "bonus", "years"]].map(lambda x: f"{x:,}")


def uppercase_strings(df: pd.DataFrame) -> pd.DataFrame:
    """将 name 和 department 列全部转大写"""
    # TODO: df[cols].map(str.upper) 或 apply(lambda s: s.str.upper())
    return df[["name", "department"]].map(str.upper)


# ── Tests ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    df = make_df()

    # Task 1
    t1 = translate_department_dict(df)
    print(f"dict map: {t1.tolist()}")
    assert t1[0] == "工程部"
    assert pd.isna(t1[t1 == "Marketing"].first_valid_index())
    print(f"dict map: {t1.tolist()}")

    t2 = translate_department_func(df)
    assert t2[0] == "工程部"
    # 无匹配时保留原值（本例所有都能匹配，加一个测试）
    test_s = pd.Series(["Engineering", "Unknown"])
    result = test_s.map(lambda x: DEPT_MAP.get(x, x))
    assert result[1] == "Unknown"
    print(f"func map: {t2.tolist()}")

    # Task 2
    l1 = salary_level_apply(df)
    assert l1[0] == "高"   # 95000
    assert l1[3] == "低"   # 55000
    assert l1[1] == "中"   # 72000
    print(f"apply salary level: {l1.tolist()}")

    l2 = salary_level_cut(df)
    assert list(l1) == list(l2), "apply 和 cut 结果应相同"
    print(f"cut salary level: {l2.tolist()}")

    # Task 3
    tc = total_compensation(df)
    assert tc[0] == 105000  # 95000 + 10000
    print(f"total compensation: {tc.tolist()}")

    stats = column_range_stats(df)
    print("\n=== 列统计 ===")
    print(stats)
    assert "salary" in stats.columns
    assert stats.loc["range", "salary"] == df["salary"].max() - df["salary"].min()

    # Task 4
    fmt = format_numbers(df)
    print(f"\n格式化数字: {fmt['salary'].tolist()}")
    assert fmt["salary"][0] == "95,000"

    up = uppercase_strings(df)
    print(f"大写: {up['name'].tolist()}")
    assert up["name"][0] == "ALICE"

    print("\n✅ All tests passed!")
