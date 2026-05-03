### `squares_of_evens(n)` → list of squares of even numbers from 0..n.
def squares_of_evens(n) -> list:
    return [ x*x for x in range(n+1) if x % 2 == 0]

### `word_lengths(words)` → dict of `{word: len(word)}` for words longer than 3 chars.
def word_lengths(words) -> dict[str, int]:
    return { word: len(word) for word in words if len(word) > 3 }   


### 3. `unique_first_letters(words)` → set of first letters of all words.
def unique_first_letters(words) -> set[str]:
    return { word[:1] for word in words if word }  # also handles empty strings

### 4. `flatten(matrix)` → flatten a 2D list using a nested comprehension.
def flatten(matrix: list[list]) -> list:
    return [elem for row in matrix for elem in row]


### 5. `transpose(matrix)` → transpose using `zip(*matrix)` AND using a comprehension.
def transpose_zip(matrix: list[list]) -> list[list]:
    return [list(row) for row in zip(*matrix)]

###6. `pair_sums(nums)` → list of `(i, j, nums[i]+nums[j])` for all `i<j`.
def pair_sums(nums: list[int]) -> list[tuple[int, int, int]]:
    return [(i, j, nums[i] + nums[j]) for i in range(len(nums)) for j in range(i+1, len(nums))]

if __name__ == "__main__":
    print(squares_of_evens(10))
    print(word_lengths(["hi", "hello", "hey", "greetings"]))
    print(unique_first_letters(["hi", "hello", "hey", "greetings"]))
    print(flatten([[1, 2], [3, 4], [5]]))  
    print(transpose_zip([[1, 2, 3], [4, 5, 6]]))
    print(pair_sums([1, 2, 3, 4]))  
    

    