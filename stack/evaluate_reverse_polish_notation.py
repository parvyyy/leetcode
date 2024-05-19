from math import ceil, floor
from typing import List
from collections import deque

def evalRPN(tokens: List[str]) -> int:
  stack = deque()

  for tok in tokens:
    # i.e. A number (-ve or +ve)
    if any(char.isdigit() for char in tok):
      stack.append(tok)
      continue
    
    # We apply the operation on the last two elements.
    n = len(stack) - 1
    expression_val = evaluate(tok, int(stack[n-1]), int(stack[n]))
    
    # Replace the two characters with the evaluated val.
    stack[n - 1] = expression_val
    stack.pop()

  return stack[0]

def evaluate(tok: str, v1: int, v2: int) -> int:
  if tok == '+':
    return v1 + v2
  elif tok == '-':
    return v1 - v2
  elif tok == '*':
    return v1 * v2
  elif tok == '/':
    res = v1 / v2
    return floor(res) if res > 0 else ceil(res)

print(evalRPN(["2","1","+","3","*"]))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))