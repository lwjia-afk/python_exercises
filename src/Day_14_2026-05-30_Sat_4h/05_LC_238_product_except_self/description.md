# LC 238 — Product of Array Except Self

- **Source**: https://leetcode.com/problems/product-of-array-except-self/
- **Difficulty**: Medium
- **Time budget**: ~30 min

## Objective
Prefix/suffix product pattern. Tests whether you can think beyond the obvious (division).

## Task
Given an integer array `nums`, return an array `answer` such that `answer[i]` equals
the product of all elements of `nums` except `nums[i]`.

**Rules:**
- Do NOT use division
- O(n) time complexity required
- O(1) extra space (the output array does not count as extra space)

## Examples
```
Input:  [1, 2, 3, 4]      →  [24, 12, 8, 6]
Input:  [-1, 1, 0, -3, 3] →  [0, 0, 9, 0, 0]
```

## Constraints
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix fits in a 32-bit integer

## Approach
**Step 1 — Left prefix pass:**
`left[i]` = product of all elements to the LEFT of index i.
`left[0] = 1` (nothing to the left).

**Step 2 — Right suffix pass (in-place):**
Traverse from right to left, keeping a running `right_product`.
Multiply `answer[i] *= right_product`, then update `right_product`.

## Self-check
- What is the time and space complexity?
- Trace through `[1, 2, 3, 4]` manually step by step.
- What happens when the array contains zeros? Does your solution handle it correctly?
