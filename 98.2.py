from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        brute force, about 6 min
        '''
        def dfs(node: TreeNode, l_limit: int, r_limit: int):
            if not node:
                return True
            if not l_limit < node.val < r_limit:
                return False
            return dfs(node.left, l_limit, node.val) and dfs(node.right, node.val, r_limit)
        return dfs(root, float('-inf'), float('inf'))
