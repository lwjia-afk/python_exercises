# LC 3 — Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s: str) -> int:
    if len(s) <= 1:
        return len(s)
    seen = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.discard(s[left])
            left += 1

        seen.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    print(lengthOfLongestSubstring("bbbbb"))     # Output: 1
    print(lengthOfLongestSubstring("pwwkew"))    # Output: 3
    print(lengthOfLongestSubstring("abba"))    # Output: 2