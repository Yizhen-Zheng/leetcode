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
        about 6 min
        '''
        def dfs(node: TreeNode, l_limit: int, r_limit: int):
            if not node:
                return True
            if not l_limit < node.val < r_limit:
                return False
            return dfs(node.left, l_limit, node.val) and dfs(node.right, node.val, r_limit)
        return dfs(root, float('-inf'), float('inf'))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        inorder: check if prev < cur
        '''
        vals = [float('-inf')]

        def dfs(node: TreeNode):
            if not node:
                return True
            valid = dfs(node.left)
            if valid and vals[-1] < node.val:
                vals.append(node.val)
                return dfs(node.right)
            return False
        return dfs(root)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        inorder: check if prev < cur
        '''

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        inorder: iterative
        '''
        s = []
        cur = root
        prev_val = float('-inf')
        while s or cur:
            if cur:
                s.append(cur)  # add mid to s
                cur = cur.left
            else:
                cur = s.pop()
                if cur.val <= prev_val:
                    return False
                prev_val = cur.val
                cur = cur.right
        return True
