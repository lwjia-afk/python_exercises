"""
LC 146 — LRU Cache
https://leetcode.com/problems/lru-cache/
Difficulty: Medium
"""

from collections import OrderedDict


# ── Approach 1: OrderedDict ─────────────────────────────────────────────────
# TODO: implement using OrderedDict
# - get: look up key, move to end (most recent), return value or -1
# - put: insert/update key, move to end, evict from front if over capacity
class LRUCache:
    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


# ── Tests ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1      # → 1
    cache.put(3, 3)               # evict key 2
    assert cache.get(2) == -1     # → -1 (evicted)
    cache.put(4, 4)               # evict key 1
    assert cache.get(1) == -1     # → -1
    assert cache.get(3) == 3      # → 3
    assert cache.get(4) == 4      # → 4

    # Edge: capacity 1
    c2 = LRUCache(1)
    c2.put(1, 1)
    c2.put(2, 2)
    assert c2.get(1) == -1
    assert c2.get(2) == 2

    print("All tests passed!")
