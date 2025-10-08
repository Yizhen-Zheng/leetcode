from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        height: to the deepest node

        '''
        def dfs(node: TreeNode):
            if not node:
                return 0, True  # height is 0
            hl, lb = dfs(node.left)
            hr, rb = dfs(node.left)
            return 1+max(hl, hr), abs(hl-hr) <= 1 and lb and rb
        _, balanced = dfs(root)
        return balanced
