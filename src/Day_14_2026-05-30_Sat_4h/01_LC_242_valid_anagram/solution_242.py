"""
LC 242 — Valid Anagram
https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
"""
from collections import Counter
from collections import defaultdict
# ── Approach 1: Counter (recommended) ──────────────────────────────────────
# TODO: implement using Counter from collections
def is_anagram_counter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


# ── Approach 2: Manual dict ─────────────────────────────────────────────────
# TODO: implement using a plain dict, no imports
def is_anagram_dict(s: str, t: str) -> bool:
    if len(s) != len(t) :
        return False
    char_dic = defaultdict(int)
    for letter in s:
        char_dic[letter] += 1
    
    for letter in t:
        char_dic[letter] -= 1
        if char_dic[letter] < 0:
            return False
    return True



# ── Tests ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    for fn in [is_anagram_counter, is_anagram_dict]:
        assert fn("anagram", "nagaram") == True
        assert fn("rat", "car") == False
        assert fn("a", "ab") == False
        assert fn("", "") == True
    print("All tests passed!")
