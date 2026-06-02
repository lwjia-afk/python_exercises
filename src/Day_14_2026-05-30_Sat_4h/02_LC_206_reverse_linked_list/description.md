# LC 206 — Reverse Linked List

- **Source**: https://leetcode.com/problems/reverse-linked-list/
- **Difficulty**: Easy
- **Time budget**: ~20 min

## Objective
Linked list basics. This is the foundation for many harder linked list problems.

## Task
Given the head of a singly linked list, reverse it and return the new head.

The `ListNode` class is already defined for you in the solution file.

Implement TWO ways:
1. **Iterative** — use three pointers: `prev`, `curr`, `next_node`. Walk through once.
2. **Recursive** — reverse the rest of the list, then fix the current node's pointer.

## Examples
```
Input:  1 -> 2 -> 3 -> 4 -> 5  →  Output: 5 -> 4 -> 3 -> 2 -> 1
Input:  1 -> 2                  →  Output: 2 -> 1
Input:  (empty)                 →  Output: (empty)
```

## Constraints
- Number of nodes: `[0, 5000]`
- `-5000 <= Node.val <= 5000`

## Hints
- Iterative: at each step, make `curr.next` point backward to `prev`, then advance both pointers.
- Recursive: `reverse(head.next)` returns the new head. Then `head.next.next = head` and `head.next = None`.

## Self-check
- Time and space complexity for each approach?
- The recursive approach uses O(n) stack space — when would that matter in production?
- Can you draw the pointer state after each step of the iterative approach on paper?
