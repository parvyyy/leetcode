from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def maxDepth(self, root: Optional[TreeNode]) -> int:
  if not root:
    return 0
  
  # Leaf node
  if root.left == None and root.right == None:
    return 1
  
  if root.left == None:
    return 1 + self.maxDepth(root.right)

  if root.right == None:
    return 1 + self.maxDepth(root.left)
  
  return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))