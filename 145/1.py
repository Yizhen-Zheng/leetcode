from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversalI(self, root: Optional[TreeNode]) -> List[int]:
        '''
        recursion: append itself last
        '''
        res = []

        def recursion(node, res):
            if not node:
                return
            recursion(node.left, res)
            recursion(node.right, res)
            res.append(node.val)
        recursion(root, res)
        return res

    def postorderTraversalII(self, root: Optional[TreeNode]) -> List[int]:
        '''
        '''
        res = []
        stack = [(root, False)]

        while stack:
            node, trace_back = stack.pop()
            if node:
                if trace_back:
                    res.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return res

    def postorderTraversalII(self, root: Optional[TreeNode]) -> List[int]:
        '''
        right-first traverse, then reverse result
        '''
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return reversed(res)
