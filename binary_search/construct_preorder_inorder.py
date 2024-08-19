from typing import Optional, List

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
  """
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    
    The first value in pre-order is the root.
    Split the pre-order list into two.
      [9] - preorder[1: (?)]
      [20, 15, 7] - preorder [(?) + 1: ]
      
      (?) is the index of the root node (3) in the inorder list.
    
    Split the in-rder list based on (?)
      
    n = CreateNode(3)
      n.left = buildTree([9], [9])
      n.right = buildTree([20, 15, 7], [15, 20, 7])
      
    Base cases:
      len() = 0: return None
      len() = 1: return createNode(l[0])
  
  """
  if len(preorder) == 0:
    return None
  
  if len(preorder) == 1:
    return TreeNode(preorder[0])
  
  root_val = preorder[0]
  n = TreeNode(root_val)
  
  # TODO: This searching increases the time complexity. Instead, create a hashmap 
  # for constant time indexing. This will result in additional complexity of the
  # following ranges, as the original list may not be pruned - as this will
  # affect the indices.
  idx = inorder.index(root_val)
  
  n.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
  n.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
  
  return n