# LC 146 — LRU Cache

- **Source**: https://leetcode.com/problems/lru-cache/
- **Difficulty**: Medium (but feels Hard — common at FAANG)
- **Time budget**: ~40 min

## Objective
Design a data structure. Tests whether you understand how to combine two structures
for O(1) on all operations. Very common in system design follow-ups too.

## Task
Implement an LRU (Least Recently Used) cache with the following interface.
All operations must be **O(1)** time complexity.

```python
class LRUCache:
    def __init__(self, capacity: int): ...

    def get(self, key: int) -> int:
        # Return the value if key exists, else -1.
        # Mark the key as most recently used.

    def put(self, key: int, value: int) -> None:
        # Insert or update the key.
        # If capacity is exceeded, evict the LEAST recently used key.
```

## Example
```
cache = LRUCache(2)
cache.put(1, 1)   # cache: {1=1}
cache.put(2, 2)   # cache: {1=1, 2=2}
cache.get(1)      # → 1,  cache: {2=2, 1=1}  (1 is now most recent)
cache.put(3, 3)   # evict 2 (LRU), cache: {1=1, 3=3}
cache.get(2)      # → -1  (evicted)
cache.put(4, 4)   # evict 1 (LRU), cache: {3=3, 4=4}
cache.get(1)      # → -1
cache.get(3)      # → 3
cache.get(4)      # → 4
```

## Two Approaches

### Approach 1 — OrderedDict (Pythonic)
Python's `OrderedDict` maintains insertion order and supports `move_to_end()`.
- `get`: look up key, call `move_to_end(key)`, return value.
- `put`: insert/update key, `move_to_end(key)`, if over capacity `popitem(last=False)`.

### Approach 2 — HashMap + Doubly Linked List (explain in interview)
A plain dict maps keys to nodes. A doubly linked list maintains order.
- Head = dummy node pointing to LRU (least recent) end.
- Tail = dummy node pointing to MRU (most recent) end.
- `get`: find node in dict, move to tail.
- `put`: add node to tail; if over capacity, remove from head and delete from dict.

**You should implement Approach 1**, but be able to **explain Approach 2** verbally
if the interviewer asks "how would you implement this without OrderedDict?"

## Self-check
- Why does O(1) require BOTH a hash map AND a doubly linked list (not singly linked)?
- What does `move_to_end(key, last=True)` do in OrderedDict?
- What does `popitem(last=False)` do?
