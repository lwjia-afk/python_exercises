# LC 3 — Longest Substring Without Repeating Characters

- **Source**: https://leetcode.com/problems/longest-substring-without-repeating-characters/
- **Difficulty**: Medium
- **Time budget**: ~40 min

## Objective
Sliding window pattern. This pattern is common — master the template.

## Task
Given a string `s`, return the length of the longest substring with no repeating characters.

Implement using the sliding-window template:
- two pointers `left`, `right`
- a `set` (or `dict` of last-seen index) to track the window contents
- expand `right`, shrink `left` when a duplicate appears

Also write a brute-force version first to anchor your understanding.

## Expected output
Pass on `'abcabcbb' → 3`, `'bbbbb' → 1`, `'pwwkew' → 3`, `'' → 0`.

## Hints
- The "shrink left" step is what makes this O(n) instead of O(n²).
- Using a `dict` of last-seen indices lets you jump `left` directly past the previous occurrence — slightly faster than incrementing.

## Self-check
- Time / space complexity?
- Can you describe the sliding-window template in one sentence?
