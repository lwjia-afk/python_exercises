"""
LC 347 — Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/
Difficulty: Medium
"""

from typing import List


# ── Approach 1: Counter + heapq ─────────────────────────────────────────────
# TODO: use Counter and heapq.nlargest — O(n log k)
def top_k_heap(nums: List[int], k: int) -> List[int]:
    pass


# ── Approach 2: Bucket sort ─────────────────────────────────────────────────
# TODO: buckets[freq] = [elements with that frequency], then collect top-k — O(n)
def top_k_bucket(nums: List[int], k: int) -> List[int]:
    pass


# ── Tests ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    for fn in [top_k_heap, top_k_bucket]:
        assert sorted(fn([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
        assert sorted(fn([1], 1)) == [1]
        assert sorted(fn([1, 2], 2)) == [1, 2]
    print("All tests passed!")
