"""
Pandas — 数据重塑 (Reshape: Pivot & Melt)
Difficulty: Medium–Hard
"""

import pandas as pd
import numpy as np


def make_sales_long() -> pd.DataFrame:
    """销售长表"""
    return pd.DataFrame({
        "date":    ["2024-Q1", "2024-Q1", "2024-Q1", "2024-Q2", "2024-Q2", "2024-Q2",
                    "2024-Q1", "2024-Q2"],
        "product": ["Laptop", "Laptop", "Mouse", "Laptop", "Mouse", "Mouse", "Monitor", "Monitor"],
        "region":  ["North", "South", "North", "North", "South", "North", "South", "North"],
        "amount":  [12000, 8000, 500, 15000, 600, 450, 3000, 3200],
    })


def make_grades_wide() -> pd.DataFrame:
    """学生成绩宽表"""
    return pd.DataFrame({
        "student_id": [1, 2, 3, 4],
        "name":       ["Alice", "Bob", "Charlie", "Dave"],
        "math":       [92, 78, 85, 91],
        "english":    [88, 82, 79, 95],
        "science":    [90, 75, 88, 87],
    })


# ── Task 1: pivot_table ──────────────────────────────────────────────────────

def sales_by_product_region(df: pd.DataFrame) -> pd.DataFrame:
    """
    行=product，列=region，值=amount 总和。
    填充缺失为 0，添加汇总行列（margins=True）。
    """
    pv = pd.pivot_table(df, index = "product", columns = "region", values = "amount", aggfunc = "sum", fill_value = 0, margins = True)
    return pv


def sales_mean_by_date_product(df: pd.DataFrame) -> pd.DataFrame:
    """
    行=date，列=product，值=amount 均值。
    不需要 margins。
    """
    return pd.pivot_table(df, index = "date", columns = "product", values = "amount", aggfunc = "mean")


# ── Task 2: melt ─────────────────────────────────────────────────────────────

def grades_wide_to_long(df: pd.DataFrame) -> pd.DataFrame:
    """
    将宽表转为长表：
    保留 student_id 和 name，
    将 math/english/science 列转为 (subject, score) 两列。
    """
    # TODO: pd.melt 或 df.melt
    return df.melt( id_vars=["student_id", "name"], value_vars=["math", "english", "science"], var_name="subject", value_name="score")


# ── Task 3: stack / unstack ───────────────────────────────────────────────────

def demo_stack(df: pd.DataFrame) -> pd.Series:
    """
    对 grades 宽表（只取成绩列）先 set_index('student_id')，
    再 stack，返回 Series（多级索引：student_id, subject）
    """
    # TODO
    df2 = df.set_index("student_id")[["math", "english", "science"]]
    return df2.stack()



def demo_unstack(stacked: pd.Series) -> pd.DataFrame:
    """将 stack 的结果 unstack 回宽表"""
    return stacked.unstack()


# ── Task 4: 综合往返转换 ──────────────────────────────────────────────────────

def roundtrip_test(df: pd.DataFrame) -> bool:
    """
    对 sales_long 做：
    1. pivot_table（行=product, 列=region, aggfunc=sum, fill_value=0）
    2. reset_index，再 melt 回长表格式
    3. 验证 melt 后 amount 总和 == 原始总和（允许 NaN 不同）
    返回 True 表示验证通过。
    提示：pivot_table 的 margins 会干扰，不要加 margins
    """
    pv = df.pivot_table(values ="amount", index="product", columns="region", aggfunc="sum", fill_value=0)
    new_pd = pd.melt(pv.reset_index(), id_vars ="product", var_name = "region", value_name="amount")
    return df["amount"].sum() == new_pd["amount"].sum()


# ── Tests ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sales = make_sales_long()
    grades = make_grades_wide()

    # Task 1
    pivot1 = sales_by_product_region(sales)
    print("=== 产品×区域 销售额 ===")
    print(pivot1)
    assert pivot1.loc["Laptop", "North"] == 27000  # 12000 + 15000
    assert "All" in pivot1.index  # margins

    pivot2 = sales_mean_by_date_product(sales)
    print("\n=== 时间×产品 均值 ===")
    print(pivot2)

    # Task 2
    long = grades_wide_to_long(grades)
    print("\n=== 成绩长表 ===")
    print(long.head(8))
    assert set(long.columns) >= {"student_id", "subject", "score"}
    assert len(long) == 4 * 3  # 4 students × 3 subjects

    # Task 3
    stacked = demo_stack(grades)
    print("\n=== stack 结果 ===")
    print(stacked.head(6))
    assert stacked.index.nlevels == 2

    unstacked = demo_unstack(stacked)
    print("\n=== unstack 回宽表 ===")
    print(unstacked)
    # 验证数值与原始一致
    orig = grades.set_index("student_id")[["math", "english", "science"]]
    assert orig.equals(unstacked[["math", "english", "science"]])

    # Task 4
    ok = roundtrip_test(sales)
    print(f"\n往返转换验证: {'✓' if ok else '✗'}")
    assert ok

    print("\n✅ All tests passed!")
