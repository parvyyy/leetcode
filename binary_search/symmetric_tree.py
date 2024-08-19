from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
  return self.checkSymmetry(root.left, root.right)

def checkSymmetry(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
  if not t1 and not t2:
    return True
  
  if not t1 or not t2:
    return False
  
  return t1.val == t2.val and self.checkSymmetry(t1.left, t2.right) and self.checkSymmetry(t1.right, t2.left) 