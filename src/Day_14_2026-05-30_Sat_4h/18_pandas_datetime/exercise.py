"""
Pandas — 日期时间处理 (DateTime)
Difficulty: Medium
"""

import pandas as pd
import numpy as np


def make_orders_df() -> pd.DataFrame:
    return pd.DataFrame({
        "order_id":    range(1, 9),
        "order_date":  ["2024-01-15", "2024-02-28", "2024-03-31",
                        "2024-04-10", "2024-05-20", "2024-06-30",
                        "bad-date",   "2024-08-15"],   # 含一个脏数据
        "ship_date":   ["2024-01-18", "2024-03-02", "2024-04-03",
                        "2024-04-15", "2024-05-25", "2024-07-05",
                        None,         "2024-08-20"],
        "amount":      [500, 1200, 800, 300, 1500, 950, 200, 600],
    })


def make_daily_sales() -> pd.DataFrame:
    """60 天的每日销售时间序列"""
    np.random.seed(7)
    dates = pd.date_range("2024-01-01", periods=60, freq="D")
    sales = np.random.normal(1000, 200, 60).clip(0)
    return pd.DataFrame({"date": dates, "sales": sales}).set_index("date")


# ── Task 1: 解析日期 ─────────────────────────────────────────────────────────

def parse_dates(df: pd.DataFrame) -> pd.DataFrame:
    """
    将 order_date 和 ship_date 转为 datetime。
    order_date 中有 'bad-date' → 用 errors='coerce' 变为 NaT
    返回新 DataFrame
    """
    # TODO
    pass


# ── Task 2: 提取属性 ─────────────────────────────────────────────────────────

def extract_date_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    假设 order_date 已是 datetime 类型。
    新增以下列（不覆盖原列）：
    - order_year, order_month, order_day
    - order_weekday（0=周一）
    - order_quarter
    - is_month_end（bool）
    """
    # TODO: df['order_date'].dt.xxx
    pass


# ── Task 3: 日期运算 ─────────────────────────────────────────────────────────

def calc_shipping_days(df: pd.DataFrame) -> pd.Series:
    """
    计算 ship_date - order_date 的天数（整数）。
    提示：两个 datetime 列相减得到 Timedelta，再 .dt.days
    """
    # TODO
    pass


def add_followup_dates(df: pd.DataFrame) -> pd.DataFrame:
    """
    新增两列：
    - followup_30d: order_date + 30 天
    - followup_1m:  order_date + 1 个月（用 pd.DateOffset(months=1)）
    """
    # TODO
    pass


# ── Task 4: 重采样 ───────────────────────────────────────────────────────────

def resample_weekly_sum(daily: pd.DataFrame) -> pd.DataFrame:
    """每周销售总和（freq='W'）"""
    # TODO
    pass


def resample_monthly_mean(daily: pd.DataFrame) -> pd.DataFrame:
    """每月销售均值（freq='ME' 或 'MS'）"""
    # TODO
    pass


# ── Task 5: 时间窗口 ─────────────────────────────────────────────────────────

def add_rolling_features(daily: pd.DataFrame) -> pd.DataFrame:
    """
    新增三列：
    - ma7:         7日移动平均
    - cumulative:  累计销售额（expanding sum）
    - lag1:        前一天销售额（shift 1）
    """
    # TODO
    pass


# ── Tests ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    df = make_orders_df()
    daily = make_daily_sales()

    # Task 1
    parsed = parse_dates(df)
    assert parsed["order_date"].dtype == "datetime64[ns]"
    assert pd.isna(parsed.loc[6, "order_date"])   # 'bad-date' → NaT
    print(f"解析后类型: {parsed['order_date'].dtype}")
    print(f"NaT 数量: {parsed['order_date'].isna().sum()}")

    # Task 2
    featured = extract_date_features(parsed.dropna(subset=["order_date"]))
    print("\n=== 日期特征 ===")
    print(featured[["order_date", "order_year", "order_month", "order_weekday", "order_quarter", "is_month_end"]].head())
    assert "order_quarter" in featured.columns
    assert featured["order_month"].iloc[0] == 1  # January

    # Task 3
    ship_days = calc_shipping_days(parsed)
    print(f"\n发货天数: {ship_days.tolist()}")
    assert ship_days.iloc[0] == 3  # Jan 15 → Jan 18

    with_followup = add_followup_dates(parsed.dropna(subset=["order_date"]))
    print(f"\n+30天: {with_followup['followup_30d'].iloc[0]}")
    print(f"+1月:  {with_followup['followup_1m'].iloc[0]}")
    assert with_followup["followup_30d"].iloc[0] == pd.Timestamp("2024-02-14")

    # Task 4
    weekly = resample_weekly_sum(daily)
    print(f"\n周度重采样行数: {len(weekly)} (60天 ≈ 8-9周)")
    assert len(weekly) <= 10

    monthly = resample_monthly_mean(daily)
    print(f"月度重采样行数: {len(monthly)}")
    assert len(monthly) == 2  # Jan + Feb

    # Task 5
    rolled = add_rolling_features(daily)
    print("\n=== 时间窗口特征（前5行）===")
    print(rolled.head(10))
    assert "ma7" in rolled.columns
    assert "cumulative" in rolled.columns
    assert "lag1" in rolled.columns
    assert pd.isna(rolled["ma7"].iloc[0])   # 前 6 行 rolling(7) 为 NaN
    assert pd.isna(rolled["lag1"].iloc[0])  # 第一行无前一天

    print("\n✅ All tests passed!")
