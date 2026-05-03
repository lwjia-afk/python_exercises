### 1. `collections.Counter` — Top 3 most common letters
from collections import Counter
def top_three_letters(text: str) -> list[tuple[str, int]]:
    count_letters = Counter(text)
    return count_letters.most_common(3)

### 2. `collections.defaultdict(list)` — Group words by length
from collections import defaultdict
def group_words_by_length(words: list[str]) -> dict[int, list[str]]:
    words_len = defaultdict(list)
    for word in words : 
        words_len[len(word)].append(word)
    return words_len

###### 3. `collections.deque` — Sliding-window queue
from collections import deque
def sliding_window_sum(k: int) -> list[int]:
    window = deque(maxlen=k)
    window.appendleft(1)  # Initialize with a zero for the first sum
    window.appendleft(2) 
    window.appendleft(3) 
    print(window)  # Output: deque([3, 2, 1], maxlen=3)
    window.appendleft(4)
    print(window)  # Output: deque([4, 3, 2], maxlen=3)
    x = window.popleft()
    print(x, window)  # Output: deque([3, 2], maxlen=3 

### 4. `itertools.combinations(nums, 2)` — All pairs
from itertools import combinations
def all_pairs(nums: list[int]) -> list[tuple[int, int]]:
    return list(combinations(nums, 2))

### 5. `itertools.permutations([1,2,3])` — All orderings
from itertools import permutations
def all_permutations(nums: list[int]) -> list[tuple[int, int, int]]:
    return list(permutations(nums, 3))

### 6. `itertools.groupby` — Group words by length (without defaultdict)
from itertools import groupby
def group_words_by_length_groupby(words: list[str]) -> dict[int, list[str]]:
    words.sort(key=len)  # Sort by length for groupby to work correctly
    grouped = {key: list(group) for key, group in groupby(words, key=len)}
    return grouped

### 7. `itertools.chain([1,2],[3,4])` — Flatten iterables
from itertools import chain
def flatten_iterables(list_of_lists: list[list[int]]) -> list[int]:
    return list(chain.from_iterable(list_of_lists)) 


if __name__ == "__main__":
    text = "hello world"
    print(top_three_letters(text))  # Output: [('l', 3), ('o', 2), ('h', 1)]   
    words = ["cat", "dog", "mouse", "rat", "bat"]
    print(group_words_by_length(words))  # Output: {3: ['cat', 'dog', 'rat', 'bat'], 5: ['mouse']}
    print(group_words_by_length_groupby(words))  # Output: {3: ['cat', 'dog', 'rat', 'bat'], 5: ['mouse']}
    nums = [1, 2, 3, 4, 5]
    k = 3  
    sliding_window_sum(k)  # Output: deque([3, 2, 1], maxlen=3) and deque([4, 3, 2], maxlen=3) and 3 deque([2, 1], maxlen=3)
    print(all_pairs(nums))  # Output: [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
    print(all_permutations([1, 2, 3]))  # Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    list_of_lists = [[1, 2], [3, 4], [5]]
    print(flatten_iterables(list_of_lists))  # Output: [1, 2