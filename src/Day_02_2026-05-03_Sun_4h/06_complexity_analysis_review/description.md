# Complexity analysis review

- **Time budget**: ~30 min

## Objective
Be able to state Big-O for any solution you write — interviewers WILL ask.

## Task
For each pattern below, write down (in `notes.md`) the time AND space complexity, then justify in one sentence.

---

### 1. Two nested loops over `nums` of size n

**Problem**: Find all pairs in `nums` that sum to a target.

Note: Different problem constraints lead to different solutions — be explicit about your assumptions when analyzing complexity.

**Variant A** — No duplicates, each pair output once (i < j):
```
Input:  nums = [1, 2, 3, 4], target = 5
Output: [[1,4], [2,3]]
```

**Variant B** — Duplicates allowed, output all matching combinations:
```
Input:  nums = [1, 4, 1, 4], target = 5
Output: [[1,4], [1,4], [1,4], [4,1]]   # or [[1,4]] × 4? depends on whether deduplication is required
```

> Do both variants have the same time complexity? What about space complexity (excluding output)?
> Which clarifying question would you ask first in an interview?

---

### 2. Iterating once and using a `set` for membership

**Problem**: Given `nums`, return `True` if any two numbers sum to `target`.

```
Input:  nums = [2, 7, 11, 15], target = 9
Output: True  (2 + 7 = 9)
```

> What is the time complexity? What is the space complexity?

---

### 3. Sorting `nums` then doing one pass

**Problem**: Count the number of unique elements in `nums`.

```
Input:  nums = [4, 2, 2, 1, 4]
Output: 3
```

> Which operation dominates: the sort or the pass? Why?

---

### 4. Recursion with branching factor 2 and depth log n

**Problem**: Binary search — find the index of `target` in a sorted array.

```
Input:  nums = [1, 3, 5, 7, 9, 11], target = 7
Output: 3
```

> How many recursive calls are made? What is the call-stack depth?

---

### 5. Recursion with branching factor 2 and depth n (naive Fibonacci)

**Problem**: Compute the nth Fibonacci number recursively.

```
Input:  n = 5
Output: 5  (sequence: 0,1,1,2,3,5)
```

> How many nodes are in this call tree? How does this compare to pattern 4?

---

### 6. Sliding window — single pass with two pointers

**Problem**: Find the length of the longest substring without repeating characters.

```
Input:  s = "abcabcbb"
Output: 3  ("abc")
```

> Each character is added and removed at most once — what does that tell you about time complexity?

---

### 7. Building a hash map from n items, then doing m lookups

**Problem**: Given a word list (n words) and query list (m words), return which queries appear in the word list.

```
Input:  words   = ["apple", "banana", "cherry"]   # n = 3
        queries = ["banana", "grape", "cherry"]   # m = 3
Output: ["banana", "cherry"]
```

> Express the total complexity in terms of both n and m.

---

## Self-check
Can you explain the difference between O(log n), O(n), O(n log n) using a real-world example?

| Complexity | Example |
|---|---|
| O(log n) | Binary search in a phone book — halve the search space each step |
| O(n) | Reading every page in a book once |
| O(n log n) | Merge sort — split n times (log n levels), process n items per level |
