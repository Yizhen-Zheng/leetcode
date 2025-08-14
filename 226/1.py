from typing import Optional
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        swap 2 child(l,r)
        5min
        t:O(n)
        s:O(logn) average, worst: O(n)(a line-like tree)
        '''
        def swap(node: TreeNode):
            if not node:
                return
            if node.left:
                swap(node.left)
            if node.right:
                swap(node.right)
            node.left, node.right = node.right, node.left
            return node
        return swap(root)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        try q
        2min
        t:O(n)
        s:O(n)(NOTE BFS require more space: last lavel contains 2/n nodes), bestcase:O(1), for a line-like tree

        '''
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                node.left, node.right = node.right, node.left
                q.append(node.left)
                q.append(node.right)
        return root
