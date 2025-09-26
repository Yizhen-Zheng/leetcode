from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''

        '''
        def dfs(node: TreeNode, d):
            if not node:
                return d
            ld = dfs(node.left, d+1)
            rd = dfs(node.right, d+1)
            return max(ld, rd)

        def dfs(node: TreeNode):
            # no need to pass d, increment during returning back
            if not node:
                return 0
            ld = 1 + dfs(node.left)
            rd = 1 + dfs(node.right)
            return max(ld, rd)
        return dfs(root)
