# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

from typing import Optional
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    
    node_level = defaultdict(list)
    q = deque()
    
    q.append((root, 0))

    while q:
        n, height = q.popleft()
        node_level[height].append(n.val)

        if n.right:
            q.append((n.right, height + 1))

        if n.left:
            q.append((n.left, height + 1))

    averages = [0] * len(node_level.keys())

    for (k, v) in node_level.items():
        averages[k] = sum(v) / len(v)

    return averages

### Key advantages -- one pass, calculating the average as it traverses.
def averageOfLevelsAlternate(root: Optional[TreeNode]) -> list[int]:
    averages = []

    q = deque()
    q.append(root)

    while q:
        nq = deque()

        total = 0
        for node in q:
            total += node.val
            if node.left: 
                nq.append(node.left)
            if node.right: 
                nq.append(node.right)
        
        averages.append(total / len(q))
        q = nq

    return averages

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(averageOfLevelsAlternate(root))