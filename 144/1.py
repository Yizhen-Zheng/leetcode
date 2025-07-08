from typing import Optional, List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversalI(self, root: Optional[TreeNode]) -> List[int]:
        '''
        preorder
        from recursion:
        '''
        res = []

        def recursion(node, res):
            if not node:
                return
            res.push(node.val)
            recursion(node.left, res)
            recursion(node.right, res)
            return
        recursion(root, res)
        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        preorder
        stack :
        '''

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
