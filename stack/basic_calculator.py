class Tokenizer:
  def __init__(self) -> None:
    self.tokens = []

  def tokenize(self, s: str) -> list:

    i = 0
    while i < len(s):
      char = s[i]
      j = 0

      if char == '(' or char == ')':
        self.tokens.append(char)
      
      if char == '+':
        self.tokens.append(char)

      if char == '-':
        # Unary operation
        if s[i + 1] == '(':
          while (i + j) < len(s) and s[i + j] != ')':
            # TODO: asd

            continue
          continue

        self.tokens.append(char)
      
      if char.isdigit():
        # Add continguous block of digits into one
        c = ''
        while (i + j) < len(s) and s[i + j].isdigit():
          c += s[i + j]

          j += 1

        self.tokens.append(c)
    
      i += max(1, j)

    return self.tokens

def calculate(s: str) -> int:
  s = s.replace(' ', '')

  stack = []

  # TODO: Tokenize
  # Without this, the offset will not work, as a evaluation of a 1-2 or 3 digit num
  # will alter the offset as they take different amount of chars. Thus we need to tokenize.
  t = Tokenizer()
  tokens = t.tokenize(s)

  # This accounts for the change in the length of s, as we evaluate expressions,
  # the brace_end is no longer at 'idx'.
  offset = 0

  for idx, char in enumerate(tokens):
    if char == ')':
      # Evaluate the string between the most recent opening bracket
      # and current closing bracket

      # 4 5 6 7 8 9 10 -> 4
      brace_start, brace_end = stack.pop(), (idx - offset)

      expr = tokens[brace_start + 1 : brace_end]

      tokens = tokens[:brace_start] + evaluate(expr) + tokens[brace_end + 1:]

      # As we are transforming the m tokens between the braces to 1, we require an offset
      offset += (brace_end - brace_start)

    elif char == '(':
      stack.append(idx - offset)


  # Now that all '(' ')' are simplified, we evaluate for a final time.
  res = evaluate(tokens)

  return int(res[0])

def evaluate(tokens: list):
  # print(s)

  num_stack = []
  op_stack = []

  for char in tokens:
    if char.isnumeric():
      num_stack.append(int(char))
    else:
      op_stack.append(char)

  res = num_stack[0]
  i,j = 1,0

  while i < len(num_stack) and j < len(op_stack):
    if op_stack[j] == '+':
      res += num_stack[i]
    elif op_stack[j] == '-':
      res -= num_stack[i]

    i += 1
    j += 1

  return [str(res)]

print(calculate("1 + 1"))
print(calculate(" 2-1 + 2 "))
print(calculate("(1+(4+5+2)-3)+(6+8)"))
print(calculate("(1+(4234+5+2)-3)+(6+8)"))