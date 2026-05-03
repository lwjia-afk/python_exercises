# LC 387 — First Unique Character in a String

- **Source**: https://leetcode.com/problems/first-unique-character-in-a-string/
- **Difficulty**: Easy
- **Time budget**: ~15 min

## Objective
Practice frequency counting with `dict` / `Counter`.

## Task
Given a string `s`, return the index of the first non-repeating character. If none, return `-1`.

Try two implementations:
1. Two-pass: build a `Counter`, then scan for the first char with count 1.
2. One-pass with `dict`: store first index, then resolve at end.

## Expected output
Both pass on `'leetcode'` → 0, `'loveleetcode'` → 2, `'aabb'` → -1.

## Self-check
What's the time/space complexity? Does the alphabet size matter?
