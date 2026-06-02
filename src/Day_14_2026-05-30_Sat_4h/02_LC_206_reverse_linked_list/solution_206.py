"""
LC 206 — Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
Difficulty: Easy
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ── Approach 1: Iterative ───────────────────────────────────────────────────
# TODO: use prev, curr, next_node pointers — O(n) time, O(1) space
def reverse_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


# ── Approach 2: Recursive ───────────────────────────────────────────────────
# TODO: O(n) time, O(n) space (call stack)
def reverse_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
       return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


# ── Helpers ─────────────────────────────────────────────────────────────────
def to_list(head: Optional[ListNode]) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def from_list(vals: list) -> Optional[ListNode]:
    if not vals:
        return None
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


# ── Tests ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    for fn in [reverse_iterative, reverse_recursive]:
        assert to_list(fn(from_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
        assert to_list(fn(from_list([1, 2]))) == [2, 1]
        assert to_list(fn(from_list([]))) == []
    print("All tests passed!")
