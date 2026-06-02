"""
LC 238 — Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
Difficulty: Medium
"""

from typing import List


# ── Approach: Prefix + Suffix in-place ─────────────────────────────────────
# TODO:
# 1. Build answer[] as left-prefix products
# 2. Do a second right-to-left pass using a running right_product variable
# Time: O(n), Space: O(1) extra
def product_except_self(nums: List[int]) -> List[int]:
    pass


# ── Tests ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([1, 1]) == [1, 1]
    print("All tests passed!")
