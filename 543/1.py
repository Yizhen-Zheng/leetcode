from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        find longest path between 2 nodes

        10:15-11:10
        55min
        t: O(n)(n nodes)
        s: O(n)(average: height)
        '''
        self.longest = 0

        def dfs(node: TreeNode):
            if not node:
                return 0
            l_depth = dfs(node.left)
            print(l_depth)
            r_depth = dfs(node.right)
            self.longest = max(self.longest, l_depth+r_depth)
            return max(l_depth, r_depth)+1
        dfs(root)
        return self.longest
