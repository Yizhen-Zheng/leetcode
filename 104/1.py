from typing import Optional
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        9:23-9:28 5min
        BFS: count
        '''
        q = deque([root])
        count = 0
        while q:
            n = len(q)
            not_empty = False
            for _ in range(n):
                node = q.popleft()
                if node:
                    not_empty = True
                    q.append(node.left)
                    q.append(node.right)
            count += (1 & not_empty)
        return count

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        DFS: need to compare
        9:28-9:30 
        '''
        def dfs(node: TreeNode):
            if not node:
                return 0
            return max(1+dfs(node.left), 1+dfs(node.right))
        return dfs(root)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        stack
        4min
        '''
        if not root:
            return 0
        s = [(root, 1)]
        count = 0
        while s:
            node, d = s.pop()
            count = max(count, d)
            if node.left:
                s.append((node.left, d+1))
            if node.right:
                s.append((node.right, d+1))
        return count
