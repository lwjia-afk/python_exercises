# LC 705 — Design HashSet

- **Source**: https://leetcode.com/problems/design-hashset/
- **Difficulty**: Easy
- **Time budget**: ~40 min

## Objective
You're being asked to BUILD a HashSet — implementing one tests:
- understanding of hash tables
- handling collisions
- class design / OOP fundamentals (init, public methods, internal state)

This is a great problem for practicing Python class structure too.

## Task
Implement `MyHashSet` with `add`, `remove`, `contains` — WITHOUT using `set` or `dict` directly.

Approach: an array of buckets, where each bucket is a list. Hash a value to a bucket index, then linear-search within the bucket.

```python
class MyHashSet:
    def __init__(self, n_buckets: int = 1009):
        self.buckets = [[] for _ in range(n_buckets)]

    def _idx(self, key: int) -> int:
        return key % len(self.buckets)

    def add(self, key: int) -> None:
        ...

    def remove(self, key: int) -> None:
        ...

    def contains(self, key: int) -> bool:
        ...
```

Discuss in code comments: load factor, why prime bucket count, when you'd resize.

## Expected output
All three operations correct. Test sequence: `add(1), add(2), contains(1)→T, contains(3)→F, add(2), contains(2)→T, remove(2), contains(2)→F`.

## Self-check
- What's the average vs worst-case time for `contains`?
- How would `MyHashMap` (LC 706) differ from this?
