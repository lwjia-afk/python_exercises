# LC 49 — Group Anagrams

- **Source**: https://leetcode.com/problems/group-anagrams/
- **Difficulty**: Medium
- **Time budget**: ~25 min

## Objective
Hash map with composite keys. The 'group by signature' pattern.

## Task
Given a list of strings, group anagrams together.

Approach:
- For each word, compute a canonical signature (e.g. sorted letters, or a 26-element count tuple).
- Use a `defaultdict(list)` keyed by signature.
- Return `list(groups.values())`.

Implement BOTH the sorted-key version AND the count-tuple version. Note which is faster theoretically (count tuple is O(k); sort is O(k log k)).

## Expected output
`['eat','tea','tan','ate','nat','bat']` → `[['eat','tea','ate'],['tan','nat'],['bat']]` (order within groups may vary).

## Self-check
What's the time complexity if there are n words of average length k?
