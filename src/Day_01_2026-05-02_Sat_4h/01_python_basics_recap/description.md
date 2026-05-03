# Python basics recap (vs .NET)

- **Time budget**: ~45 min

## Objective
Refresh Python core data types and idioms, mapped from your .NET mental model:

| .NET / C#                 | Python                                       |
|---------------------------|----------------------------------------------|
| `List<T>`                 | `list` (mutable, `[]`)                       |
| `T[]`                     | `tuple` (immutable, `()`)                    |
| `Dictionary<K,V>`         | `dict` (`{}`)                                |
| `HashSet<T>`              | `set`                                         |
| `string.Substring(i,n)`   | `s[i:i+n]`                                    |
| `LINQ Where/Select`       | list/dict/set comprehensions, generators     |
| `foreach`                 | `for x in iterable`                          |
| `Nullable<T>`             | `Optional[T]` / `None`                       |

## Task
Open `practice.py` (create it). Implement and run the following:

---

### 1. First 10 squares — list comprehension

Using a list comprehension, generate a list of the squares of integers 1 through 10.

**Input:** none (hardcoded range)

**Expected output:**
```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

---

### 2. Letter → position dict

Build a `dict` that maps every lowercase letter `'a'`–`'z'` to its 1-indexed position in the alphabet.

**Input:** none (use `string.ascii_lowercase` or `range`)

**Expected output (first 5 shown):**
```
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, ..., 'z': 26}
```

---

### 3. Count occurrences — manual loop vs Counter

Given the list `["a", "b", "a", "c", "b", "a"]`, count how many times each element appears.
Implement it **two ways**: a manual `for` loop, and `collections.Counter`.

**Input:**
```python
words = ["a", "b", "a", "c", "b", "a"]
```

**Expected output (both methods):**
```
{'a': 3, 'b': 2, 'c': 1}
{'a': 3, 'b': 2, 'c': 1}
```

---

### 4. String slicing — extract `"view"` two ways

Given the string `"interview"`, extract the substring `"view"` using two different slice expressions.

**Input:**
```python
s = "interview"
```

**Expected output (both slices):**
```
view
view
```

Hint: `"interview"` has 9 characters. `"view"` starts at index 5 and is the last 4 characters.

---

### 5. Tuple unpacking with `*rest`

Unpack the list `[1, 2, 3, 4, 5]` so that `a=1`, `b=2`, and `rest` gets everything else.
Print all three variables.

**Input:**
```python
data = [1, 2, 3, 4, 5]
```

**Expected output:**
```
a = 1
b = 2
rest = [3, 4, 5]
```

---

### 6. `is` vs `==`

Create two separate list variables with the same contents `[1, 2, 3]`.
Print the result of both `==` and `is` comparisons and explain why they differ.

**Input:**
```python
x = [1, 2, 3]
y = [1, 2, 3]
```

**Expected output:**
```
x == y  → True   (same value)
x is y  → False  (different objects in memory)
```

## Expected output
- `print` statements show correct results for each step.
- You can explain (out loud) the difference between `list`, `tuple`, `set`, `dict`.
- You can explain why `is` is identity and `==` is equality.

## Self-check
- When would you choose `tuple` over `list`?
- What's the time complexity of `x in list` vs `x in set`?
- What does `dict.get(key, default)` do that `dict[key]` doesn't?
