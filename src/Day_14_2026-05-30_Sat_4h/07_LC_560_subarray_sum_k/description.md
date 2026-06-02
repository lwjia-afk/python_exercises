# LC 560 — Subarray Sum Equals K

- **Source**: https://leetcode.com/problems/subarray-sum-equals-k/
- **Difficulty**: Medium
- **Time budget**: ~35 min

## Objective
Prefix sum + HashMap. This is a high-frequency interview pattern that trips up
candidates who reach for sliding window (which doesn't work when negatives are present).

## Task
Given an integer array `nums` and an integer `k`, return the total number of
**contiguous subarrays** whose sum equals `k`.

## Examples
```
Input:  nums = [1, 1, 1],  k = 2  →  2
Input:  nums = [1, 2, 3],  k = 3  →  2   (subarrays: [1,2] and [3])
Input:  nums = [1, -1, 1], k = 1  →  3
```

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`
- Note: the array CAN contain negative numbers → sliding window does NOT work

## Why Sliding Window Fails
Sliding window works when all values are non-negative (expanding right increases sum,
shrinking left decreases it). With negatives, there's no monotonic relationship.

## The Prefix Sum Approach — Key Insight
Let `prefix[i]` = sum of `nums[0..i]`.
A subarray `nums[i+1..j]` sums to `k` iff:
```
prefix[j] - prefix[i] = k
→ prefix[i] = prefix[j] - k
```
So: walk through the array, maintain a running prefix sum and a HashMap of
`{prefix_sum: count}`. At each step, check if `(current_prefix - k)` is in the map.

Don't forget to initialize the map with `{0: 1}` (empty prefix).

## Self-check
- Trace through `[1, 1, 1]`, `k=2` step by step. What is in the map at each step?
- Why do we initialize `prefix_count = {0: 1}`?
- Time and space complexity?
