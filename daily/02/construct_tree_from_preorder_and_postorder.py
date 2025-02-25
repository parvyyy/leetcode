# 23/02/25
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/

from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructFromPrePost(preorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
    pre, post = deque(preorder), deque(postorder)

    def construct():
        curr = TreeNode(pre.popleft())

        if curr.val != post[0]:
            curr.left = construct()

        if curr.val != post[0]:
            curr.right = construct()

        post.popleft()

        return curr
        
    return construct()

print(constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1]))