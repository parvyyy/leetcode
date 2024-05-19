from collections import deque

def isClosing(char: str) -> bool:
  return char == '}' or char == ')' or char == ']'

def isOpening(char: str) -> bool:
  return char == '{' or char == '(' or char == '['

def isMatchingParenthesis(c1, c2):
  if c1 == '(' and c2 == ')':
    return True
  
  if c1 == '{' and c2 == '}':
    return True
  
  if c1 == '[' and c2 == ']':
    return True

  return False

def isValid(s: str) -> bool:
  stack = deque()

  for char in s:
    if isClosing(char):
      # If the stack is empty, it is not possible for a closing brace to have a corresponding
      # opening.
      if not stack:
        return False
      
      # We want the current closing char to be a pair with the most recent opening char
      areMatching = isMatchingParenthesis(stack.pop(), char)

      if not areMatching:
        return False
      
    if isOpening(char):
      stack.append(char)


  # Return True only if each opening brace had a matching closing brace.
  return len(stack) == 0


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))