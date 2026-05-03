from collections import Counter, defaultdict

### 1. First 10 squares — list comprehension
def first_10_squares():
    return [i**2 for i in range(10)]

### 2. Letter → position dict
def letter_position_dict() -> dict[str, int] :
    return{ chr(i): i for i in range(97, 123) }


### 3. Count occurrences — manual loop vs Counter
def count_occurrences_manual(lst) -> dict[str, int] :
    res = {}
    for item in lst:
        res[item] = res.get(item, 0) +1
    return res

def count_occurrences_counter(lst) -> dict[str, int] :
    return dict(Counter(lst))

def count_occurrences_defaultdict(lst) -> dict[str, int] :
    res = defaultdict(int)
    for item in lst:
        res[item] += 1
    return dict(res)


### 4. String slicing — extract `"view"` two ways
### Hint: `"interview"` has 9 characters. `"view"` starts at index 5 and is the last 4 characters.

def extract_view_slice(s: str) -> tuple[str, str]:
    pos = s[5:]
    neg = s[-4:]

    return pos, neg


### 5. Tuple unpacking with `*rest`
def tuple_unpacking_example():
    a, b, *rest = (1, 2, 3, 4, 5)
    return a, b, rest


### 6. `is` vs `==`




if __name__ == "__main__":
    print(first_10_squares())
    print(letter_position_dict())
    sample_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
    print(count_occurrences_manual(sample_list))
    print(count_occurrences_counter(sample_list))
    print(count_occurrences_defaultdict(sample_list))
    print(extract_view_slice("interview"))
    print(tuple_unpacking_example())