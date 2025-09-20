from collections import deque
from typing import Optional, List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        7:35-7:49
        omg it's wrong cuz not appending a pair of children, but that layer!!!


        if not root:
            return []
        q = deque([root])
        ans = [[root.val]]
        while q:
            parent = q.pop()
            l, r = parent.left, parent.right
            if l or r:
                ans.append([])
                if l:
                    ans[-1].append(l.val)
                    q.append(l)
                if r:
                    ans[-1].append(r.val)
                    q.append(r)
        return ans

        6min, 7:49-54
        use list and replace seems faster
        '''
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            cur_layer = len(q)
            ans.append([])
            for _ in range(cur_layer):
                parent = q.popleft()
                ans[-1].append(parent.val)
                l, r = parent.left, parent.right
                if l:
                    q.append(l)
                if r:
                    q.append(r)
        return ans

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            cur_layer_vals = []
            next_layer = []
            for parent in q:
                cur_layer_vals.append(parent.val)
                l, r = parent.left, parent.right
                if l:
                    next_layer.append(l)
                if r:
                    next_layer.append(r)
            ans.append(cur_layer_vals)
            q = next_layer
        return ans
