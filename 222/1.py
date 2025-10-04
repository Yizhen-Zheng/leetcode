from typing import Optional, List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        '''
        8:22-8:52
        10:35-11:02

        '''
        if not root:
            return 0

        def dfs(node: TreeNode, count: int):
            if node.right is None and node.left is None:
                # cannot confirm where the edge of leaf layer is
                return count, False
            # find the spot where we can confirm count completed
            elif node.right is None and node.left:
                return count*2, True
            # is not leaf(has both right and left child) try to find imbalanced point
            new_count_r, find_edge_r = dfs(node.right, count*2+1)
            if find_edge_r:
                return new_count_r, True
            new_count_l, find_edge_l = dfs(node.left, count*2)
            if find_edge_l:
                return new_count_l, True
            if new_count_l > new_count_r:
                return new_count_l, True
            return new_count_r, False
        count, _ = dfs(root, 1)
        return count

    def countNodes(self, root: Optional[TreeNode]) -> int:
        '''
        watch solution
        t: O(logn * logn)
        s: O(logn) ?
        '''
        if not root:
            return 0

        def count_l_depth(node: TreeNode):
            if not node:
                return 0
            return 1+count_l_depth(node.left)

        def count_r_depth(node: TreeNode):
            if not node:
                return 0
            return 1+count_r_depth(node.right)

        def dfs(node: TreeNode):
            l_depth, r_depth = count_l_depth(node), count_r_depth(node)
            if l_depth == r_depth:
                return (1 << r_depth)-1

            return 1+dfs(node.left)+dfs(node.right)

        count = dfs(root)
        return count

    def countNodes(self, root: Optional[TreeNode]) -> int:
        def find_depth(node: TreeNode):  # always go left
            if not node:
                return 0
            return 1+find_depth(node.left)

        def count(node: TreeNode):
            if not node:
                return 0
            l_depth, r_depth = find_depth(node.left), find_depth(node.right)
            if l_depth == r_depth:
                # node and left:(1 << l_depth), right: count r
                return (1 << l_depth) + count(node.right)
            # when right = left-1:
            # node and right: (1<<r_depth), left: count l
            return (1 << r_depth) + count(node.left)
        return count(root)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        def find_left_d(node: TreeNode):  # find left most d
            if not node:
                return 0
            return find_left_d(node.left)+1

        def find_right_d(node: TreeNode):  # find right most d
            if not node:
                return 0
            return find_right_d(node.right)+1

        def count(node: TreeNode):
            l_depth, r_depth = find_left_d(node), find_right_d(node)
            if l_depth == r_depth:
                return (1 << l_depth)-1
            return 1 + count(node.left) + count(node.right)
        return count(root)
