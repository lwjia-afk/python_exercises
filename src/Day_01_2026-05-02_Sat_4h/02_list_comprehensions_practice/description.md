# List / dict / set comprehensions drill

- **Time budget**: ~30 min

## Objective
Get fluent with comprehensions — they show up constantly in Python interviews and in pandas/PySpark UDFs.

## Data
None — work in `practice.py`.

## Task
Solve each WITHOUT using a `for` loop with `.append()`:

1. `squares_of_evens(n)` → list of squares of even numbers from 0..n.
   - Input: `n = 10`
   - Output: `[0, 4, 16, 36, 64, 100]`

2. `word_lengths(words)` → dict of `{word: len(word)}` for words longer than 3 chars.
   - Input: `["hi", "hello", "world", "cat", "python"]`
   - Output: `{"hello": 5, "world": 5, "python": 6}`

3. `unique_first_letters(words)` → set of first letters of all words.
   - Input: `["apple", "banana", "avocado", "cherry"]`
   - Output: `{"a", "b", "c"}`

4. `flatten(matrix)` → flatten a 2D list using a nested comprehension.
   - Input: `[[1, 2, 3], [4, 5], [6, 7, 8, 9]]`
   - Output: `[1, 2, 3, 4, 5, 6, 7, 8, 9]`

5. `transpose(matrix)` → transpose using `zip(*matrix)` AND using a comprehension.
   - Input: `[[1, 2, 3], [4, 5, 6]]`
   - Output: `[[1, 4], [2, 5], [3, 6]]`

6. `pair_sums(nums)` → list of `(i, j, nums[i]+nums[j])` for all `i<j`.
   - Input: `[10, 20, 30]`
   - Output: `[(0, 1, 30), (0, 2, 40), (1, 2, 50)]`

## Expected output
All six functions implemented and tested with at least 2 inputs each.

## Self-check
- When is a generator expression preferable to a list comprehension?
- What's the equivalent LINQ for `[x*2 for x in xs if x>0]`?
