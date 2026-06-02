# LC 242 — Valid Anagram

- **Source**: https://leetcode.com/problems/valid-anagram/
- **Difficulty**: Easy
- **Time budget**: ~15 min

## Objective
Practice `Counter` and character frequency comparison.

## Task
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, else `False`.
An anagram uses exactly the same letters as the original, just rearranged.

Implement TWO ways:
1. Using `Counter` from `collections` — one-liner comparison.
2. Using a plain `dict` to count characters manually (no imports).

## Examples
```
Input:  s = "anagram", t = "nagaram"  →  True
Input:  s = "rat",     t = "car"      →  False
Input:  s = "a",       t = "ab"       →  False  (different lengths)
```

## Constraints
- `1 <= len(s), len(t) <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters only

## Self-check
- What is the time and space complexity of each approach?
- What if the strings contained Unicode characters (e.g. Chinese)? Does your solution still work?
- Can you do it in O(1) space? (Hint: sort both strings and compare — what's the trade-off?)
