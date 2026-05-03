###Given a string `s`, return the index of the first non-repeating character. If none, return `-1`.
from collections import Counter

def firstUniqChar(s: str) -> int:
    char_count = Counter(s)
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index
    return -1

def firstUniqCharWithDict(s: str) -> int:
    res = {}
    seen = set()
    for i in range(len(s)):
        letter = s[i]
        if letter in seen: 
            res.pop(letter, None)
        else:
            seen.add(letter)
            res[letter] = i
    if len(res) > 0:
        return min(res.values())
    return -1
        

if __name__ == "__main__":
    print(firstUniqChar("leetcode"))  # Output: 0
    print(firstUniqChar("loveleetcode"))  # Output: 2
    print(firstUniqChar("aabb"))  # Output: -1
    print(firstUniqCharWithDict("leetcode"))  # Output: 0
    print(firstUniqCharWithDict("loveleetcode"))  # Output: 2
    print(firstUniqCharWithDict("aabb"))  # Output: -1