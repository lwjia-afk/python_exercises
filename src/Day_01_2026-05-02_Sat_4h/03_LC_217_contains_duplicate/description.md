# LC 217 — Contains Duplicate

- **Source**: https://leetcode.com/problems/contains-duplicate/
- **Difficulty**: Easy
- **Time budget**: ~15 min

## Objective
Warmup. Practice using `set` for O(n) membership checks.

## Task
Given an integer array `nums`, return `True` if any value appears at least twice, else `False`.

Implement TWO ways:
1. Using a `set` in a single pass (O(n) time, O(n) space).
2. Using `len(nums) != len(set(nums))` (one-liner — discuss its trade-offs).

## Expected output
`solution.py` with both implementations and a quick test block.

## Self-check
- Why is the `set`-based approach faster than nested loops?
- Can you do it without extra space? (Yes, by sorting — what's the time complexity?)
