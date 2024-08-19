from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
  # Perform the same traversal of both trees - checking equality.
  if not p and not q:
    return True
  
  if not p:
    return False
  
  if not q:
    return False
  
  return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)