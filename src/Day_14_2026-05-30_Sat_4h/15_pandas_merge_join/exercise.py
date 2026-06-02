"""
Pandas — 合并与连接 (Merge & Join)
Difficulty: Medium
"""

import pandas as pd


def make_employees() -> pd.DataFrame:
    return pd.DataFrame({
        "emp_id":  [1, 2, 3, 4, 5],
        "name":    ["Alice", "Bob", "Charlie", "Dave", "Eve"],
        "dept_id": [10, 20, 10, 30, 99],   # 99 = 不存在的部门
        "salary":  [95000, 72000, 88000, 55000, 61000],
    })


def make_departments() -> pd.DataFrame:
    return pd.DataFrame({
        "dept_id":   [10, 20, 30, 40],   # 40 = 无员工的部门
        "dept_name": ["Engineering", "Marketing", "HR", "Finance"],
        "budget":    [500000, 300000, 200000, 400000],
    })


def make_orders() -> pd.DataFrame:
    return pd.DataFrame({
        "order_id":    [101, 102, 103, 104],
        "customer_id": [1, 2, 1, 3],
        "product_id":  [11, 12, 13, 11],
        "quantity":    [2, 1, 3, 1],
    })


def make_customers() -> pd.DataFrame:
    return pd.DataFrame({
        "customer_id":   [1, 2, 3],
        "customer_name": ["Acme Corp", "Beta Ltd", "Gamma Inc"],
    })


def make_products() -> pd.DataFrame:
    return pd.DataFrame({
        "product_id":   [11, 12, 13],
        "product_name": ["Laptop", "Mouse", "Monitor"],
        "unit_price":   [1200.0, 25.0, 300.0],
    })


# ── Task 1: 四种 join ────────────────────────────────────────────────────────

def inner_join(emp: pd.DataFrame, dept: pd.DataFrame) -> pd.DataFrame:
    """inner join on dept_id"""
    # TODO
    new_df = emp.merge(dept, on="dept_id", how="inner")
  
    return new_df


def left_join(emp: pd.DataFrame, dept: pd.DataFrame) -> pd.DataFrame:
    """left join：保留所有员工"""
    # TODO
    new_df = emp.merge(dept, on = "dept_id", how="left")
    return new_df


def find_unmatched_employees(emp: pd.DataFrame, dept: pd.DataFrame) -> pd.DataFrame:
    """
    找出没有对应部门的员工（Eve，dept_id=99）。
    提示：left join + indicator=True，然后过滤 _merge == 'left_only'
    """
    # TODO
    new_df = emp.merge(dept, on="dept_id", how="left", indicator=True)
    unmatched = new_df[new_df["_merge"] == "left_only"]
    return unmatched[["emp_id", "name", "dept_id"]]


def outer_join(emp: pd.DataFrame, dept: pd.DataFrame) -> pd.DataFrame:
    """outer join：保留所有员工和所有部门"""
    return emp.merge(dept, on = "dept_id", how="outer")


# ── Task 2: 列名冲突处理 ─────────────────────────────────────────────────────

def merge_with_custom_suffixes(df1: pd.DataFrame, df2: pd.DataFrame,
                                on: str, suffixes: tuple) -> pd.DataFrame:
    """
    合并两个有同名列的 DataFrame，使用自定义后缀。
    示例：合并后的列名应是 score_exam1 和 score_exam2（而非 score_x, score_y）
    """
    df = df1.merge(df2, on = on, suffixes = suffixes)
    return df


# ── Task 3: concat ───────────────────────────────────────────────────────────

def concat_quarters(q1: pd.DataFrame, q2: pd.DataFrame) -> pd.DataFrame:
    """
    纵向 concat，重置索引，并新增 quarter 列标识来源（'Q1' or 'Q2'）。
    不要用 keys 参数，而是手动新增列，更实用。
    """
    df_q1 = q1.copy()
    df_q1["quarter"] = "Q1"
    df_q2 = q2.copy()
    df_q2["quarter"] = "Q2"
    combined = pd.concat([df_q1, df_q2], ignore_index=True)
    return combined


def concat_with_multiindex(q1: pd.DataFrame, q2: pd.DataFrame) -> pd.DataFrame:
    """
    纵向 concat，用 keys=['Q1','Q2'] 创建多级索引。
    返回结果并打印，理解多级索引结构。
    """
    df_q1 = q1.copy()
    df_q1["quarter"] = "Q1"
    df_q2 = q2.copy()
    df_q2["quarter"] = "Q2"
    combined = pd.concat([df_q1, df_q2], keys=["Q1", "Q2"])
    return combined


# ── Task 4: 多表关联 ─────────────────────────────────────────────────────────

def build_order_report(orders: pd.DataFrame,
                       customers: pd.DataFrame,
                       products: pd.DataFrame) -> pd.DataFrame:
    """
    链式 merge，最终返回包含以下列的 DataFrame：
    order_id, customer_name, product_name, quantity, unit_price, total_amount
    其中 total_amount = quantity * unit_price
    """
    df = orders.merge(customers, on = "customer_id", how = "inner").merge(products, on ="product_id", how = "inner")
    df["total_amount"] = df["quantity"] * df["unit_price"]
    return df[["order_id", "customer_name", "product_name", "quantity", "unit_price", "total_amount"]]    

# ── Tests ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    emp = make_employees()
    dept = make_departments()

    # Task 1
    inner = inner_join(emp, dept)
    print(f"Inner join 行数: {len(inner)} (期望 4，排除 Eve 和 Finance)")
    assert len(inner) == 4

    left = left_join(emp, dept)
    print(f"Left join 行数: {len(left)} (期望 5，所有员工)")
    assert len(left) == 5
    assert left[left["name"] == "Eve"]["dept_name"].isna().all()

    unmatched = find_unmatched_employees(emp, dept)
    print(f"无部门员工: {unmatched['name'].tolist()}")
    assert list(unmatched["name"]) == ["Eve"]

    outer = outer_join(emp, dept)
    print(f"Outer join 行数: {len(outer)} (期望 6，所有员工+Finance)")
    assert len(outer) == 6

    # Task 2
    df_a = pd.DataFrame({"id": [1, 2], "score": [90, 80], "grade": ["A", "B"]})
    df_b = pd.DataFrame({"id": [1, 2], "score": [85, 75], "comment": ["Good", "OK"]})
    merged = merge_with_custom_suffixes(df_a, df_b, on="id", suffixes=("_exam1", "_exam2"))
    print(f"\n自定义后缀列名: {list(merged.columns)}")
    assert "score_exam1" in merged.columns
    assert "score_exam2" in merged.columns

    # Task 3
    q1 = emp[["name", "salary"]].copy()
    q1["revenue"] = [100, 200, 150, 80, 120]
    q2 = emp[["name", "salary"]].copy()
    q2["revenue"] = [110, 220, 160, 90, 130]

    combined = concat_quarters(q1, q2)
    print(f"\nConcat 行数: {len(combined)} (期望 10)")
    assert len(combined) == 10
    assert "quarter" in combined.columns

    multi = concat_with_multiindex(q1, q2)
    print(f"多级索引层数: {multi.index.nlevels}")
    assert multi.index.nlevels == 2

    # Task 4
    orders = make_orders()
    customers = make_customers()
    products = make_products()
    report = build_order_report(orders, customers, products)
    print("\n=== 订单报告 ===")
    print(report)
    assert "total_amount" in report.columns
    assert report.loc[report["order_id"] == 101, "total_amount"].values[0] == 2400.0

    print("\n✅ All tests passed!")
