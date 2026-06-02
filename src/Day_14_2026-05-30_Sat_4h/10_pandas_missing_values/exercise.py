"""
Pandas — 缺失值处理 (Missing Values)
Difficulty: Easy–Medium
"""

import pandas as pd
import numpy as np


def make_sales_df() -> pd.DataFrame:
    """带缺失值的销售数据"""
    np.random.seed(42)
    return pd.DataFrame({
        "order_id": range(1, 11),
        "product":   ["A", "B", None, "A", "C", "B", None, "A", "C", "B"],
        "quantity":  [5, None, 3, None, 2, 8, 4, None, 6, 1],
        "price":     [100.0, 200.0, 150.0, None, 300.0, None, 200.0, 100.0, None, 200.0],
        "discount":  [0.1, None, None, 0.2, None, 0.15, None, None, 0.05, None],
        "region":    ["North", "South", None, "North", None, "East", "South", None, "East", "North"],
    })


def make_sensor_df() -> pd.DataFrame:
    """时间序列传感器数据"""
    dates = pd.date_range("2024-01-01", periods=10, freq="D")
    values = [10.0, None, None, 13.0, None, 15.0, None, 17.0, None, 19.0]
    return pd.DataFrame({"date": dates, "reading": values}).set_index("date")


# ── Task 1: 检测缺失值 ──────────────────────────────────────────────────────

def missing_summary(df: pd.DataFrame) -> pd.DataFrame:
    """返回每列的 missing_count 和 missing_pct（0~1）"""
    df_summary = pd.DataFrame({
        "missing_count": df.isna().sum(),
        "missing_pct" : df.isna().mean()
    })
    return df_summary



def rows_with_any_missing(df: pd.DataFrame) -> pd.DataFrame:
    """返回任意列有缺失的行"""
    return df.loc[df.isna().any(axis=1)]  # type: ignore[index]



def rows_with_all_missing(df: pd.DataFrame) -> pd.DataFrame:
    """返回所有列都缺失的行（本例不存在，返回空 DataFrame 即可）"""
    return df.loc[df.isna().all(axis=1)]  # type: ignore[index]


# ── Task 2: 删除缺失值 ──────────────────────────────────────────────────────

def drop_high_missing_cols(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """删除缺失率超过 threshold 的列"""
    return df.loc[:, df.isna().mean() <= threshold]  # type: ignore[index]



def drop_rows_missing_key_cols(df: pd.DataFrame, key_cols: list) -> pd.DataFrame:
    """删除 key_cols 中任意一列有缺失的行"""
    return df.dropna(subset=key_cols)

def drop_rows_not_in_missing_key_cols(df: pd.DataFrame, key_cols: list) -> pd.DataFrame:
    """删除 非key_cols 中任意一列有缺失的行"""
    cols = [c for c in df.columns if c not in key_cols]
    return df.dropna(subset = cols)


# ── Task 3: 填充缺失值 ──────────────────────────────────────────────────────

def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    按业务规则填充：
    - discount  → 0
    - price     → 中位数
    - quantity  → 先 ffill，再 bfill
    - region    → 众数
    返回新 DataFrame，不修改原始数据
    """
    new_df = df.copy()
    new_df["discount"] = df["discount"].fillna(0)
    new_df["price"] = df["price"].fillna(df["price"].median())
    new_df["quantity"] = df["quantity"].ffill().bfill()
    new_df["region"] = df["region"].fillna(df["region"].mode()[0])
    return new_df



# ── Task 4: 插值 ────────────────────────────────────────────────────────────

def compare_interpolation(df: pd.DataFrame) -> pd.DataFrame:
    """
    对 sensor DataFrame 分别用 linear 和 time 插值，
    返回包含 reading_linear 和 reading_time 两列的 DataFrame
    """
    res = df.copy()
    res["reading_linear"] = res["reading"].interpolate("linear")
    res["reading_time"] = res["reading"].interpolate("time")    
    return res


# ── Tests ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    df = make_sales_df()

    # Task 1
    summary = missing_summary(df)
    print("=== Missing Summary ===")
    print(summary)
    assert "missing_count" in summary.columns
    assert "missing_pct" in summary.columns

    any_missing = rows_with_any_missing(df)
    print(f"\n行数（任意列缺失）: {len(any_missing)}")
    assert len(any_missing) > 0

    all_missing = rows_with_all_missing(df)
    print(f"行数（全部列缺失）: {len(all_missing)}")
    assert len(all_missing) == 0

    # Task 2
    dropped_cols = drop_high_missing_cols(df, threshold=0.5)
    print(f"\n删除高缺失列后剩余列: {list(dropped_cols.columns)}")

    dropped_rows = drop_rows_missing_key_cols(df, ["product", "quantity"])
    print(f"删除关键列缺失行后剩余: {len(dropped_rows)} 行")

    # Task 3
    filled = fill_missing_values(df)
    print("\n=== 填充后缺失值数量 ===")
    print(filled[["discount", "price", "quantity", "region"]].isna().sum())
    assert filled["discount"].isna().sum() == 0
    assert filled["price"].isna().sum() == 0
    assert filled["quantity"].isna().sum() == 0
    assert filled["region"].isna().sum() == 0

    # Task 4
    sensor = make_sensor_df()
    interp = compare_interpolation(sensor)
    print("\n=== 插值对比 ===")
    print(interp)

    print("\n✅ All tests passed!")
