# LC 283 — Move Zeroes

- **Source**: https://leetcode.com/problems/move-zeroes/
- **Difficulty**: Easy
- **Time budget**: ~20 min

## Objective
Two-pointer technique with in-place mutation.

## Task
Given `nums`, move all `0`s to the end while preserving the relative order of non-zero elements. Do it IN PLACE without making a copy.

Approach:
- `write` pointer at 0; iterate `read` from 0..n-1
- if `nums[read] != 0`: swap `nums[write]` with `nums[read]` and `write += 1`

Avoid the trap of overwriting then padding with zeros — it works but loses style points.

## Expected output
`[0,1,0,3,12] → [1,3,12,0,0]`, `[0] → [0]`.

## Self-check
Why is the swap version preferable to the overwrite-then-pad version?
