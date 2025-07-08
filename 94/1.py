from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversalI(self, root: Optional[TreeNode]) -> List[int]:
        '''
        left ->middle ->right
        rec:
        '''
        res = []

        def recursion(node, res):
            if not node:
                return
            recursion(node.left, res)
            res.append(node.val)
            recursion(node.right, res)
        recursion(root, res)
        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        left ->middle ->right
        stack:
        (node, trace_back)
        '''
        res = []
        stack = [(root, False)]

        while stack:
            node, trace_back = stack.pop()
            if node:
                if trace_back:
                    res.append(node.val)
                    continue
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))

        return res
