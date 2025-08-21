# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        16:49-16:55
        t: O(logn)(tree height)
        s: O(logn)(tree height)
        '''
        lo, hi = min(p.val, q.val), max(p.val, q.val)

        def dfs(node: TreeNode):
            print(node.val)
            if lo <= node.val <= hi:
                return node
            if node.val < lo:
                return dfs(node.right)
            if node.val > hi:
                return dfs(node.left)
        lca = dfs(root)
        return lca

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        solution: iterative
        16:57-16:59
        t: O(logn)
        s: O(1)

        '''
        lo, hi = min(p.val, q.val), max(p.val, q.val)
        node = root
        while root:
            if lo <= node.val <= hi:
                return node
            if node.val < lo:
                node = node.right
            if node.val > hi:
                node = node.left
        # return node
