# LC 167 — Two Sum II (Sorted Input)

- **Source**: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
- **Difficulty**: Medium
- **Time budget**: ~20 min

## Objective
Two-pointer technique on sorted arrays — a frequently-asked variation of Two Sum.

## Task
Given a 1-indexed sorted array `numbers`, return the 1-based indices of the two numbers that add up to `target`.

Approach:
- `left = 0, right = len-1`
- if `numbers[left] + numbers[right] == target`: done
- if sum too small: `left += 1`
- if sum too big: `right -= 1`

Constraint: O(1) extra space (no hash map).

Return `[left+1, right+1]` (the problem uses 1-indexing).

## Expected output
`[2,7,11,15], target=9` → `[1,2]`.

## Self-check
Why does the two-pointer approach require the array to be sorted?
