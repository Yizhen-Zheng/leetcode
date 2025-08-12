# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        brute-force: traverse all branches until null or not balanced
        9min+8min
        never differ more than one! 

        this below is misunderstanding!!!
        # if not root:
        #     return True
        # q = deque([root])
        # count = 1
        # while q:
        #     if len(q) < count:
        #         node = q.popleft()
        #         if node != None and (node.left != None or node.right != None):
        #             return False
        #         continue
        #     for _ in range(count):
        #         node = q.popleft()
        #         if node:
        #             q.append(node.left)
        #             q.append(node.right)
        #     count <<= 1
        # return True
        mid order traverse to compare left and right!!!
        '''
        # 10:03-10:18, 15min
        # DFS, t: O(n)(visit every node once), s: O(logn)
        def rec(node: TreeNode, depth):
            if not node:
                # print(node)
                return depth, True
            # print(node.val)
            depth_l, balanced_l = rec(node.left, depth+1)
            if not balanced_l:
                return depth_l, False
            depth_r, balanced_r = rec(node.right, depth+1)
            return max(depth_l, depth_r), (balanced_l and balanced_r and abs(depth_l-depth_r) < 2)
        max_depth, balanced = rec(root, 0)
        # print(max_depth)
        return balanced

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        try other solution
        '''
