# LC 347 — Top K Frequent Elements

- **Source**: https://leetcode.com/problems/top-k-frequent-elements/
- **Difficulty**: Medium
- **Time budget**: ~30 min

## Objective
Frequency counting + heap. A pattern that appears constantly in DS interviews.

## Task
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.
You may return the answer in any order.

## Examples
```
Input:  nums = [1, 1, 1, 2, 2, 3],  k = 2  →  [1, 2]
Input:  nums = [1],                  k = 1  →  [1]
```

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is always valid: `1 <= k <= number of unique elements`
- The answer is unique (only one valid result)
- **Required**: better than O(n log n)

## Implement TWO ways
1. **Counter + heapq.nlargest** — clean, Pythonic. What is the time complexity?
2. **Bucket sort** — create a list of buckets where `bucket[freq]` holds elements
   with that frequency. Iterate from high to low frequency. O(n) time.

## Hints
- `Counter(nums).most_common(k)` works but read the docs — what does it return?
- For bucket sort: max possible frequency is `len(nums)`, so bucket size = `len(nums) + 1`.

## Self-check
- Why is bucket sort O(n) while heap is O(n log k)?
- When would you prefer the heap approach over bucket sort in a real system?
