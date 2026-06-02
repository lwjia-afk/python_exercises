"""
LC 560 — Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/
Difficulty: Medium
"""

from typing import List


# ── Approach: Prefix Sum + HashMap ──────────────────────────────────────────
# TODO:
# - Initialize prefix_count = {0: 1}
# - Walk through nums, maintaining a running prefix sum
# - At each step: count += prefix_count.get(prefix - k, 0)
# - Then: prefix_count[prefix] += 1
# Time: O(n), Space: O(n)
def subarray_sum(nums: List[int], k: int) -> int:
    pass


# ── Tests ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2
    assert subarray_sum([1, -1, 1], 1) == 3
    assert subarray_sum([1], 1) == 1
    assert subarray_sum([1], 0) == 0
    print("All tests passed!")
