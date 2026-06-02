"""
Pandas — 字符串操作 (String Operations)
Difficulty: Easy–Medium
"""

import pandas as pd
import numpy as np


def make_products_df() -> pd.DataFrame:
    return pd.DataFrame({
        "product_code": ["ELEC_001", "CLOTH_042", "FOOD_003", "ELEC_015", "HOME_007"],
        "product_name": ["  Laptop Pro ", "Cotton T-Shirt", "ORGANIC MILK", "wireless mouse", "Coffee Maker"],
        "sku":          ["SKU-1001-A", "SKU-2042-B", "SKU-3003-C", "SKU-1015-D", "SKU-4007-E"],
        "tags":         ["new,sale,featured", "sale", "organic,food", "new,electronic", None],
    })


LOG_LINES = pd.Series([
    "[2024-01-15 10:23:45] ERROR user_id=123 message=login_failed",
    "[2024-02-20 14:05:12] INFO  user_id=456 message=page_view",
    "[2024-03-10 09:00:00] WARN  user_id=789 message=slow_query",
    "[2024-04-05 16:30:00] ERROR user_id=101 message=db_timeout",
])


# ── Task 1: 基础操作 ─────────────────────────────────────────────────────────

def normalize_product_names(df: pd.DataFrame) -> pd.Series:
    """
    对 product_name 列：
    1. strip 前后空格
    2. 统一为 Title Case（每个单词首字母大写）
    """
    # TODO
    pass


def product_name_lengths(df: pd.DataFrame) -> pd.Series:
    """返回 product_name 每个值的字符长度（strip 之后）"""
    # TODO
    pass


# ── Task 2: 切割与提取 ────────────────────────────────────────────────────────

def extract_category(df: pd.DataFrame) -> pd.Series:
    """
    从 product_code（如 'ELEC_001'）提取 '_' 前的类别部分：'ELEC'
    方法1：str.split('_').str[0]
    """
    # TODO
    pass


def split_sku(df: pd.DataFrame) -> pd.DataFrame:
    """
    将 sku（如 'SKU-1001-A'）拆分为三列：sku_prefix, sku_number, sku_suffix
    用 str.split('-', expand=True)
    """
    # TODO
    pass


def extract_sku_number(df: pd.DataFrame) -> pd.Series:
    """
    用正则从 sku 中提取 4 位数字部分（如 '1001'），返回字符串 Series。
    提示：str.extract(r'(\d{4})')
    """
    # TODO
    pass


# ── Task 3: 判断与过滤 ────────────────────────────────────────────────────────

def filter_electronics(df: pd.DataFrame) -> pd.DataFrame:
    """返回 product_code 以 'ELEC' 开头的行"""
    # TODO: str.startswith
    pass


def has_sale_tag(df: pd.DataFrame) -> pd.Series:
    """
    返回 bool Series：tags 列是否包含 'sale'。
    注意 tags 有 NaN，用 na=False。
    """
    # TODO: str.contains('sale', na=False)
    pass


# ── Task 4: 解析日志 ──────────────────────────────────────────────────────────

def parse_log_lines(logs: pd.Series) -> pd.DataFrame:
    """
    解析 LOG_LINES，提取为 DataFrame，列为：
    - timestamp: 字符串 '2024-01-15 10:23:45'（后续可转 datetime）
    - level:     'ERROR' / 'INFO' / 'WARN'
    - user_id:   整数
    - message:   'login_failed' 等

    提示：用 str.extract 配合正则捕获组
    参考正则：r'\[(.+?)\]\s+(\w+)\s+user_id=(\d+)\s+message=(\S+)'
    """
    # TODO
    pass


# ── Task 5: NaN 安全操作 ──────────────────────────────────────────────────────

def safe_tag_filter(df: pd.DataFrame, tag: str) -> pd.DataFrame:
    """返回 tags 列包含指定 tag 的行（NaN 行安全跳过）"""
    # TODO
    pass


# ── Tests ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    df = make_products_df()

    # Task 1
    names = normalize_product_names(df)
    assert names[0] == "Laptop Pro"          # 去掉首尾空格 + Title Case
    assert names[2] == "Organic Milk"         # 全大写 → Title Case
    assert names[3] == "Wireless Mouse"       # 全小写 → Title Case
    print(f"normalize: {names.tolist()}")

    lengths = product_name_lengths(df)
    assert lengths[0] == len("Laptop Pro")
    print(f"lengths: {lengths.tolist()}")

    # Task 2
    cats = extract_category(df)
    assert list(cats) == ["ELEC", "CLOTH", "FOOD", "ELEC", "HOME"]
    print(f"categories: {cats.tolist()}")

    split = split_sku(df)
    assert list(split.columns) == ["sku_prefix", "sku_number", "sku_suffix"]
    assert split["sku_prefix"][0] == "SKU"
    assert split["sku_suffix"][0] == "A"
    print(f"split SKU:\n{split}")

    sku_nums = extract_sku_number(df)
    assert sku_nums[0] == "1001"
    print(f"sku numbers: {sku_nums.tolist()}")

    # Task 3
    elec = filter_electronics(df)
    assert len(elec) == 2
    print(f"electronics: {elec['product_code'].tolist()}")

    sale_mask = has_sale_tag(df)
    assert sale_mask[0] == True   # 'new,sale,featured'
    assert sale_mask[2] == False  # 'organic,food'
    assert sale_mask[4] == False  # NaN → False
    print(f"has_sale: {sale_mask.tolist()}")

    # Task 4
    parsed = parse_log_lines(LOG_LINES)
    print("\n=== 解析日志 ===")
    print(parsed)
    assert list(parsed.columns) == ["timestamp", "level", "user_id", "message"]
    assert parsed["level"][0] == "ERROR"
    assert parsed["user_id"][0] == "123"  # 字符串形式，可进一步 astype(int)

    # Task 5
    new_items = safe_tag_filter(df, "new")
    assert len(new_items) == 2  # ELEC_001 和 ELEC_015
    assert None not in new_items["tags"].tolist()
    print(f"\n'new' tag 商品: {new_items['product_code'].tolist()}")

    print("\n✅ All tests passed!")
