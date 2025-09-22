from collections import deque
from typing import Optional, List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        5:27-5:39
        12min
        '''
        if not root:
            return []
        ans = []
        q = [root]
        reverse_vals = False
        while q:
            children = []
            cur_vals = []
            for parent in q:
                cur_vals.append(parent.val)
                if parent.left:
                    children.append(parent.left)
                if parent.right:
                    children.append(parent.right)
            ans.append(list(reversed(cur_vals)) if reverse_vals else cur_vals)
            reverse_vals = not reverse_vals
            q = children

        return ans

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        manually reverse
        why both condition need reverse:
        the previously reversed layer(left to right) causes next layer is also layout l to r
        so need to reverse when loop
        '''
        if not root:
            return []
        ans = []
        q = [root]
        reverse_vals = False
        while q:
            children = []
            cur_vals = []
            for parent in reversed(q):
                if not reverse_vals:
                    cur_vals.append(parent.val)
                    if parent.left:
                        children.append(parent.left)
                    if parent.right:
                        children.append(parent.right)
                else:
                    cur_vals.append(parent.val)
                    if parent.right:
                        children.append(parent.right)
                    if parent.left:
                        children.append(parent.left)
            ans.append(cur_vals)
            reverse_vals = not reverse_vals
            q = children
        return ans
