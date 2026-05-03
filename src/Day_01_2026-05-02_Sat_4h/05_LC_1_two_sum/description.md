# LC 1 — Two Sum

- **Source**: https://leetcode.com/problems/two-sum/
- **Difficulty**: Easy
- **Time budget**: ~20 min

## Objective
The canonical hash-map-for-O(n) problem. You'll be asked to talk through this in interviews.

## Task
Given `nums: list[int]` and `target: int`, return indices of the two numbers that add up to `target`.

Implement:
1. Brute force O(n²) — for completeness.
2. Single-pass hash map O(n).

Be ready to explain the trade-off out loud.

## Expected output
`solution.py` with both, tests for `[2,7,11,15], 9 → [0,1]`.

## Self-check
- Why does the hash map approach work in one pass?
- What if the input has duplicates? Negative numbers?
