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

    def inorderTraversalII(self, root: Optional[TreeNode]) -> List[int]:
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

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        left ->middle ->right
        stack:
        without trace back
        if current is not leaf node: add current path to stack, to left 
        if reached bottom, find prev(the leaf node, which is middle of 2 none children), 
            add to res, go right
            then find none again, back to last second layer, repeat go right
        '''
        res = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res
