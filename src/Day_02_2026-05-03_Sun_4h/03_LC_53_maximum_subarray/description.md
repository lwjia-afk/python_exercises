# LC 53 — Maximum Subarray

- **Source**: https://leetcode.com/problems/maximum-subarray/
- **Difficulty**: Medium
- **Time budget**: ~40 min

## Objective
Kadane's algorithm — your first taste of dynamic programming. Crucial.

## Task
Given an integer array `nums`, find the contiguous subarray with the largest sum and return that sum.

Implement Kadane's algorithm:
- `current = max(nums[i], current + nums[i])`
- `best = max(best, current)`

Then explain (in code comments) WHY this works: at each index you decide whether to extend the previous subarray or start fresh.

## Expected output
Pass on `[-2,1,-3,4,-1,2,1,-5,4] → 6`, `[1] → 1`, `[5,4,-1,7,8] → 23`.

## Self-check
- Time / space complexity?
- How would you also return the actual subarray (not just the sum)?
