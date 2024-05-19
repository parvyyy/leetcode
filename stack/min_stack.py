class MinStack:
    def __init__(self):
      self.stack = []
      self.minStack = []
      
    def push(self, val: int) -> None:
      self.stack.append(val)

      # minStack represents a 'version history' of minimum values
      if not self.minStack:
        self.minStack.append(val)
        return
      
      self.minStack.append(min(self.minStack[-1], val))

    def pop(self) -> None:
      self.stack.pop()
      self.minStack.pop()

    def top(self) -> int:
      return self.stack[-1]
    
    def getMin(self) -> int:
      return self.minStack[-1]