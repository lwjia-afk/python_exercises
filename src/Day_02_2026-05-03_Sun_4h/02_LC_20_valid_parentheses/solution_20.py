# LC 20 — Valid Parentheses 
def isValid(s: str) -> bool:
    opener = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in s:
      if char in opener.keys():
          stack.append(char)
      elif char in opener.values():
          if not stack :
              return False
          if opener[stack.pop(-1)] != char :
              return False  
    return not stack

if __name__ == "__main__":
    print(isValid("()"))        # Output: True
    print(isValid("()[]{}"))    # Output: True
    print(isValid("(]"))        # Output: False
    print(isValid("([)]"))      # Output: False
    print(isValid("{[]}"))      # Output: True