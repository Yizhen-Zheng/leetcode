from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        '''
        10:11-10:29, TLE, 18mins
        seems still O(n^2), or O(2^n)?  
        time: O(2^n)(every node computes its subtree entirely) -> 2^n / 2
        cuz for every node, the compute amount doubles

        brute-force: try all(for a node, rob or not)
        for a node and its sub-tree, there're 2 option: rob or not

        '''
        def dfs(node: TreeNode, can_rob: bool):
            if not node:
                return 0
            if not can_rob:
                return dfs(node.left, True)+dfs(node.right, True)
            not_pick = dfs(node.left, True)+dfs(node.right, True)
            pick = node.val+dfs(node.left, False)+dfs(node.right, False)
            return max(not_pick, pick)
        res = dfs(root, True)
        return res

    def rob(self, root: Optional[TreeNode]) -> int:
        '''
        for a node and its sub-tree, there're 2 option: rob or not
        memo
        10:29-10:41 12min
        '''
        def dfs(node: TreeNode, can_rob: bool):
            if not node:
                return 0
            if not hasattr(node, 'not_pick'):
                node.not_pick = dfs(node.left, True)+dfs(node.right, True)
            if not hasattr(node, 'pick'):
                node.pick = node.val+dfs(node.left, False)+dfs(node.right, False)
            return max(node.not_pick, node.pick) if can_rob else node.not_pick
        res = dfs(root, True)
        return res

    def rob(self, root: Optional[TreeNode]) -> int:
        '''
        watch ans
        O(n)
        '''
        def dfs(node: TreeNode):
            if not node:
                return (0, 0)  # pick, not pick
            l, r = dfs(node.left), dfs(node.right)
            # pick cur:
            pick_cur = node.val+l[1]+r[1]
            not_pick_cur = max(l)+max(r)
            return pick_cur, not_pick_cur
        pick_root, not_pick_root = dfs(root)
        return max(pick_root, not_pick_root)
