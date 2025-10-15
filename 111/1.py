from typing import Optional
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        '''
        6:12-6:35
        23min
        omg this is traversing all nodes down to the deepest one!
        '''
        if not root:
            return 0

        def dfs(node: TreeNode, d):
            if not node:
                return inf
            if node.left is None and node.right is None:
                return d
            ld = dfs(node.left, d+1)
            rd = dfs(node.right, d+1)
            return min(ld, rd)
        mind = dfs(root, 1)
        return mind

    def minDepth(self, root: Optional[TreeNode]) -> int:
        '''
        solution BFS: reach the nearest leaf node and stop
        or use deq, append(node, depth)
        '''
        if not root:
            return 0
        q = [root]
        d = 0
        while q:
            children = []
            d += 1
            for node in q:
                if node.left is None and node.right is None:
                    return d
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            q = children
        return d
