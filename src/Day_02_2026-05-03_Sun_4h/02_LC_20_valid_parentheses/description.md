# LC 20 — Valid Parentheses

- **Source**: https://leetcode.com/problems/valid-parentheses/
- **Difficulty**: Easy
- **Time budget**: ~25 min

## Objective
Stack pattern. Trivial-looking, but interviewers love it because it tests if you reach for the right data structure.

## Task
Given a string of `()[]{}`, return whether brackets are balanced and properly nested.

Implementation:
- use a `list` as a stack (`append` / `pop`)
- map closer → opener with a dict
- on closer: if stack top doesn't match, return False
- at end: stack must be empty

## Expected output
Pass on `'()' → True`, `'()[]{}' → True`, `'(]' → False`, `'([)]' → False`, `'' → True`.

## Self-check
What if the string contains other characters? (Edge case to clarify with interviewer.)
