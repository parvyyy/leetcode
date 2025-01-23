# https://leetcode.com/problems/binary-tree-right-side-view/description/

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    
    rsv = []

    q, visited = deque(), set()
    q.append((root, 0))

    # BFS - O(V) time complexity
    while q:
        n, height = q.popleft()

        if height not in visited:
            rsv.append(n.val)
            visited.add(height)

        if n.right:
            q.append((n.right, height + 1))

        if n.left:
            q.append((n.left, height + 1))

    return rsv




