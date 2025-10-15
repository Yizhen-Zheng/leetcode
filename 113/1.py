from typing import Optional, List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        '''
        way to mark as invalid
        6:4?-7:10, around 25-30 min
        rather than checking not none, maybe just handle a basic condition that cur node is none in dfs
        this makes code much simpler
        '''
        if not root:
            return []
        ans = []

        def dfs(node: TreeNode, path: list[int], acc: int):
            acc += node.val  # add to current state
            find = False
            if node.left or node.right:  # not leaf
                path.append(node.val)
                if node.left:
                    find |= dfs(node.left, path, acc)
                if node.right:
                    find |= dfs(node.right, path, acc)
                path.pop()
                return find

            else:  # is leaf
                if acc == targetSum:
                    path.append(node.val)
                    ans.append(path[:])
                    path.pop()
                    return True
                return False

        dfs(root, [], 0)
        return ans
