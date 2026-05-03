# Python string manipulation drill

- **Time budget**: ~15 min

## Objective
Strings come up everywhere. Get the built-ins to muscle memory.

## Task
In `practice.py`, implement using ONLY built-in string methods (no regex):

---

### 1. `is_palindrome(s: str) -> bool`
Case-insensitive, ignoring spaces and punctuation.

```
Input:  "A man a plan a canal Panama"
Output: True

Input:  "race a car"
Output: False

Input:  "Was it a car or a cat I saw?"
Output: True
```

---

### 2. `reverse_words(s: str) -> str`
Reverse the order of words; handle extra whitespace gracefully.

```
Input:  "hello world"
Output: "world hello"

Input:  "  the sky   is blue  "
Output: "blue is sky the"

Input:  "a"
Output: "a"
```

---

### 3. `count_vowels(s: str) -> int`
Count a e i o u, case-insensitive.

```
Input:  "Hello World"
Output: 3

Input:  "rhythm"
Output: 0

Input:  "AEIOU"
Output: 5
```

---

### 4. `kebab_to_snake(s: str) -> str`
Replace every `-` with `_`.

```
Input:  "foo-bar-baz"
Output: "foo_bar_baz"

Input:  "my-variable-name"
Output: "my_variable_name"

Input:  "already_snake"
Output: "already_snake"
```

---

### 5. `truncate(s: str, n: int, suffix: str = '...') -> str`
Return at most `n` total characters. If the string is longer than `n`, cut it and append `suffix` (the suffix counts toward `n`).

```
Input:  s="Hello, World!", n=8
Output: "Hello..."        # 5 chars kept + "..." = 8

Input:  s="Hi", n=10
Output: "Hi"              # no truncation needed

Input:  s="Python", n=6
Output: "Python"          # exactly n, no truncation

Input:  s="Python", n=4, suffix="…"
Output: "Pyt…"            # 3 chars kept + "…" = 4
```

---

## Self-check
What's the difference between `str.split()` (no arg) and `str.split(' ')`?
