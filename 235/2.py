# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        brute-force
        '''
        if p.val > q.val:  # make p<q
            p, q = q, p

        def dfs(node: TreeNode):
            if node is None:
                return None
            print(node.val)
            # if p.val <= node.val <= q.val:# same as below
            if node == p or node == q or p.val < node.val < q.val:
                return node
            if node.val > q.val:  # p<q<n
                return dfs(node.left)
            else:  # n<p<q
                return dfs(node.right)
        return dfs(root)
