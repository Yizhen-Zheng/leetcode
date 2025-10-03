from typing import Optional, List
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        '''
        7:59-8:08
        has root
        '''
        q = [root]
        space = False
        while q:
            children = []
            for parent in q:
                if not parent:
                    space = True
                    continue
                if space:
                    return False
                children.append(parent.left)
                children.append(parent.right)
            q = children
        return True
