"""
Pandas — 异常值检测与处理 (Outliers)
Difficulty: Medium
"""

import pandas as pd
import numpy as np


def make_df() -> pd.DataFrame:
    np.random.seed(0)
    n = 100
    df = pd.DataFrame({
        "user_id":          range(1, n + 1),
        "age":              np.random.randint(18, 65, n),
        "purchase_amount":  np.random.normal(200, 40, n),
        "session_duration": np.random.normal(30, 8, n),
    })
    # 手动注入异常值
    df.loc[5,  "purchase_amount"] = 1500   # 极大值
    df.loc[10, "purchase_amount"] = -200   # 极小值（负购买额）
    df.loc[20, "session_duration"] = 300   # 极长会话
    return df

def add_outliers_iqr(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    同时在返回 DataFrame 中附加 lower_bound 和 upper_bound 列（方便调试）。
    """
    res = df.copy()
    q1 = res[col].quantile(0.25)
    q3 = res[col].quantile(0.75)
    iqr = q3 - q1
    res["lower_bound"] = q1 - 1.5 * iqr
    res["upper_bound"] = q3 + 1.5 * iqr
    
    return res



# ── Task 1: IQR 方法 ────────────────────────────────────────────────────────

def detect_outliers_iqr(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    返回 col 列中 IQR 方法判定为异常的行。
    同时在返回 DataFrame 中附加 lower_bound 和 upper_bound 列（方便调试）。
    """
    res = df.copy()
    q1 = res[col].quantile(0.25)
    q3 = res[col].quantile(0.75)
    iqr = q3 - q1
    res["lower_bound"] = q1 - 1.5 * iqr
    res["upper_bound"] = q3 + 1.5 * iqr
    return res.loc[(res[col] > res["upper_bound"]) | (res[col] < res["lower_bound"])]
    


# ── Task 2: Z-score 方法 ────────────────────────────────────────────────────

def detect_outliers_zscore(df: pd.DataFrame, col: str, threshold: float = 3.0) -> pd.DataFrame:
    """
    返回 |z-score| > threshold 的行。
    手动计算 z-score（不依赖 scipy）。
    """
    res = df.copy()
    res["z_score"] = (res[col] - res[col].mean())/res[col].std()
    return res.loc[(res["z_score"] > threshold) | (res["z_score"] < threshold * -1)]


# ── Task 3: 三种处理策略 ────────────────────────────────────────────────────

def remove_outliers(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """直接删除 IQR 方法判定为异常的行"""
    res = df.copy()
    q1 = res[col].quantile(0.25)
    q3 = res[col].quantile(0.75)
    iqr = q3 - q1
    upper = q3 + iqr * 1.5
    lower = q1 - iqr * 1.5
    
    return res.loc[(res[col] <= upper) & (res[col] >= lower)]


def clip_outliers(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    截断：超出 [Q1-1.5*IQR, Q3+1.5*IQR] 的值替换为边界值。
    提示：用 df[col].clip(lower, upper)
    """
    res = df.copy()
    q1 = res[col].quantile(0.25)
    q3 = res[col].quantile(0.75)
    iqr = q3 - q1
    upper = q3 + 1.5 * iqr
    lower = q1 - 1.5 * iqr
    
    res[col] = res[col].clip(lower = lower, upper = upper)
    return res


def replace_outliers_with_nan(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """将 IQR 异常值替换为 NaN"""
    res = df.copy()
    q1 = res[col].quantile(0.25)
    q3 = res[col].quantile(0.75)
    iqr = q3 - q1
    upper = q3 + 1.5 * iqr
    lower = q1 - 1.5 * iqr
    
    res[col] = res[col].where((res[col] < upper) & (res[col] > lower), other = np.nan)

    return res



# ── Task 4: 批量多列检测 ────────────────────────────────────────────────────

def detect_all_outliers_iqr(df: pd.DataFrame) -> dict:
    """
    对所有 numeric 列运行 IQR 检测。
    返回 {col_name: list_of_outlier_indices}
    跳过 user_id 这类 ID 列（提示：可以只处理非 ID 列）
    """
    outliers = {}

    numeric_cols = df.select_dtypes(include="number").columns
    cols = [c for c in numeric_cols if "id" not in c.lower()]
    for col in cols:
        res = add_outliers_iqr(df, col)
        mask = (res[col] > res["upper_bound"]) | (res[col] < res["lower_bound"])
        outliers[col] = res.index[mask].tolist()
    
    return outliers
    


# ── Tests ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    df = make_df()

    # Task 1
    iqr_outliers = detect_outliers_iqr(df, "purchase_amount")
    print("=== IQR 异常值 (purchase_amount) ===")
    print(iqr_outliers[["user_id", "purchase_amount", "lower_bound", "upper_bound"]])
    assert 5 in iqr_outliers.index   # 注入的极大值
    assert 10 in iqr_outliers.index  # 注入的极小值

    # Task 2
    z_outliers = detect_outliers_zscore(df, "purchase_amount")
    print("\n=== Z-score 异常值 (purchase_amount) ===")
    print(z_outliers[["user_id", "purchase_amount"]])

    # Task 3
    df_removed = remove_outliers(df, "purchase_amount")
    print(f"\n删除后行数: {len(df_removed)} (原始: {len(df)})")
    assert 5 not in df_removed.index

    df_clipped = clip_outliers(df, "purchase_amount")
    q1 = df["purchase_amount"].quantile(0.25)
    q3 = df["purchase_amount"].quantile(0.75)
    iqr = q3 - q1
    assert df_clipped["purchase_amount"].max() <= q3 + 1.5 * iqr + 1e-9
    print(f"截断后最大值: {df_clipped['purchase_amount'].max():.2f}")

    df_nan = replace_outliers_with_nan(df, "purchase_amount")
    print(f"替换为 NaN 后缺失数: {df_nan['purchase_amount'].isna().sum()}")

    # Task 4
    all_outliers = detect_all_outliers_iqr(df)
    print("\n=== 批量检测结果 ===")
    for col, idx in all_outliers.items():
        print(f"  {col}: {len(idx)} 个异常值 → indices {idx}")

    print("\n✅ All tests passed!")
