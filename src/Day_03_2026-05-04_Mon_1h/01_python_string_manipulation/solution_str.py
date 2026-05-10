### 1. `is_palindrome(s: str) -> bool`
def is_palindrome(s: str) -> bool:
    cleanStr = s.replace(" ","")
    return cleanStr == cleanStr[::-1]

### 2. `reverse_words(s: str) -> str`
def reverse_words(s: str) -> str:
    words = [word for word in s.split()]
    return " ".join(words[::-1])

### 3. `count_vowels(s: str) -> int`
def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

### 4. `kebab_to_snake(s: str) -> str`
def kebab_to_snake(s: str) -> str:
    return s.replace("-", "_")


if __name__ == "__main__":
    # Test cases for is_palindrome
    print(is_palindrome("A man a plan a canal Panama"))  # True
    print(is_palindrome("Hello World"))  # False        
    # Test cases for reverse_words
    print(reverse_words("Hello World  for     test"))  # "World Hello"    
    print(reverse_words("Python is great"))  # "great is Python"
    # Test cases for count_vowels   
    print(count_vowels("Hello World"))  # 3
    print(count_vowels("Python is great"))  # 4
    # Test cases for kebab_to_snake
    print(kebab_to_snake("hello-world"))  # "hello_world"
    print(kebab_to_snake("kebab-case-string"))  # "kebab_case_string"
    