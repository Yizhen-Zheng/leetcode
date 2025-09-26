from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        5:27-5:39, 6:15-6:17
        12+2=14min
        cannot rely on arr length
        '''
        if not root:
            return 0
        max_width = 0  # update every layer
        q = [(root, 1)]
        while q:
            children = []
            for parent, pos in q:
                if parent.left:

                    children.append((parent.left, pos*2-1))
                if parent.right:
                    children.append((parent.right, pos*2))
            l, r = q[0][1], q[-1][1]
            w = r-l+1
            max_width = max(max_width, w)
            q = children
        return max_width
