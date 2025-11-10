# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        early prune?
        count num
        13min ish
        '''
        def dfs(upper: int, node: TreeNode) -> int:
            if not node:
                return 0
            is_good = node.val >= upper
            upper = max(upper, node.val)
            count_l, count_r = dfs(upper, node.left), dfs(upper, node.right)
            return is_good+count_l+count_r
        return dfs(root.val, root)
