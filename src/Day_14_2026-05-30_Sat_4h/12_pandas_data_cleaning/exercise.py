"""
Pandas — 数据清洗 (Data Cleaning)
Difficulty: Easy–Medium
"""

import pandas as pd
import numpy as np


def make_dirty_df() -> pd.DataFrame:
    return pd.DataFrame({
        "user_id":   [1, 2, 3, 2, 4, 5, 5],
        "name":      ["Alice", "Bob", "Charlie", "Bob", "Dave", "Eve", "Eve"],
        "age":       ["25", "30", "unknown", "30", "45", "28", "28"],
        "price":     ["$100.5", "$200", "$150", "$200", "$300", "$250", "$250"],
        "is_active": ["True", "False", "yes", "False", "no", "True", "True"],
        "date":      ["2024-01-15", "15/01/2024", "2024-03-10", "15/01/2024", "2024-05-20", "10/06/2024", "10/06/2024"],
        "category":  ["  Electronics ", "electronics", "ELECTRONICS", "electronics", "Clothing", "clothing", "clothing"],
        "email":     ["alice@example.com", "bob_no_at", "charlie@test.com", "bob_no_at", "dave@mail.com", "eve@site.org", "eve@site.org"],
        "phone":     ["138-1234-5678", "13812345678", "(138)12345678", "13812345678", "138-9876-5432", "139-0000-1111", "139-0000-1111"],
    })


# ── Task 1: 重复行 ───────────────────────────────────────────────────────────

def find_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """返回所有重复行（keep=False，即重复组的每一行都返回）"""
    return df[df.duplicated(keep = False)]


def dedup_by_subset(df: pd.DataFrame, subset: list, keep: str = "first") -> pd.DataFrame:
    """基于 subset 列去重，重置索引"""
    res = df.drop_duplicates(subset = subset, keep = "first").reset_index(drop = True)
    return res


# ── Task 2: 数据类型转换 ─────────────────────────────────────────────────────

def clean_age(df: pd.DataFrame) -> pd.Series:
    """将 age 列转为 numeric，'unknown' 变 NaN，类型为 float（因为有 NaN）"""
    return pd.to_numeric(df["age"], errors="coerce")


def clean_price(df: pd.DataFrame) -> pd.Series:
    """去掉 $ 符号，转为 float"""
    return pd.to_numeric(df["price"].astype(str).str.replace("$", ""), errors="coerce")


def clean_is_active(df: pd.DataFrame) -> pd.Series:
    """统一映射为 bool：True/'True'/'yes' → True，False/'False'/'no' → False"""
    mapping = {"True": True, "False": False, "yes": True, "no": False}
    return df["is_active"].map(mapping)


def clean_date(df: pd.DataFrame) -> pd.Series:
    """混合日期格式 → datetime64，用 dayfirst 处理 dd/mm/yyyy"""
    dates=  pd.to_datetime(df["date"], format='mixed', dayfirst=True, errors="coerce")
    return dates
# ── Task 3: 字符串规范化 ─────────────────────────────────────────────────────

def normalize_category(df: pd.DataFrame) -> pd.Series:
    """strip + 首字母大写，统一为 'Electronics', 'Clothing' 等"""
    # TODO: str.strip().str.title() 或 str.capitalize()
    return df["category"].str.strip().str.title()


def filter_valid_emails(df: pd.DataFrame) -> pd.DataFrame:
    """删除 email 列中不含 '@' 的行"""
    df = df[df["email"].str.contains("@", na=False)]
    return df.reset_index(drop = True)

import re

def normalize_phone(series: pd.Series) -> pd.Series:
    """
    将所有手机号统一为 'XXX-XXXX-XXXX' 格式。
    输入可能是：'13812345678', '(138)12345678', '138-1234-5678'
    提示：先用 str.replace 去掉所有非数字，再重新格式化
    """
    phone = series.astype(str).str.replace(r"\D", "", regex=True)
    return phone.str.replace(r"(\d{3})(\d{4})(\d{4})", r"\1-\2-\3", regex=True)
    


# ── Task 4: 列名清洗 ─────────────────────────────────────────────────────────

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    将列名统一为 snake_case 小写，去掉特殊字符。
    示例列名：["First Name", "Age (years)", "Email Address", "Is Active?"]
    期望输出：["first_name", "age_years", "email_address", "is_active"]
    """
    res = df.copy()
    res.columns = (df.columns
                   .str.replace(r"[^A-Za-z0-9 ]", "", regex = True)
                   .str.strip()
                   .str.lower()
                   .str.replace(" ", "_"))
    return res


# ── Tests ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    df = make_dirty_df()

    # Task 1
    dups = find_duplicates(df)
    print(f"重复行数: {len(dups)}")
    assert len(dups) == 4  # user_id 2 和 5 各出现 2 次

    deduped = dedup_by_subset(df, ["user_id"])
    print(f"去重后行数: {len(deduped)}")
    assert len(deduped) == 5

    # Task 2
    age = clean_age(df)
    assert pd.isna(age[2])
    assert age[0] == 25.0
    print(f"age 类型: {age.dtype}, 示例: {age.tolist()}")

    price = clean_price(df)
    assert price[0] == 100.5
    print(f"price 示例: {price.tolist()}")

    active = clean_is_active(df)
    assert active[0] == True
    assert active[2] == True
    assert active[4] == False
    print(f"is_active 示例: {active.tolist()}")

    dates = clean_date(df)
    assert dates.dtype == "datetime64[us]"
    print(f"date 示例: {dates.tolist()[:3]}")

    # Task 3
    cat = normalize_category(df)
    assert cat.iloc[0] == "Electronics"
    assert cat.iloc[1] == "Electronics"
    print(f"category 统一后: {cat.unique()}")

    valid_email_df = filter_valid_emails(df)
    assert all(valid_email_df["email"].str.contains("@"))
    print(f"有效 email 行数: {len(valid_email_df)}")

    phones = normalize_phone(df["phone"])
    assert all(phones.str.match(r"\d{3}-\d{4}-\d{4}"))
    print(f"phone 统一格式: {phones.tolist()}")

    # Task 4
    messy = pd.DataFrame(columns=["First Name", "Age (years)", "Email Address", "Is Active?"])
    cleaned = clean_column_names(messy)
    print(f"清洗后列名: {list(cleaned.columns)}")
    assert list(cleaned.columns) == ["first_name", "age_years", "email_address", "is_active"]

    print("\n✅ All tests passed!")
