from typing import Optional, List
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        5:13-6:03
        50min 
        + 
        7:07-7:28
        21min
        = 71min 
        seems: use inorder to get leaf node
        '''
        n = len(inorder)
        used_val = set()
        p, i = deque(preorder), deque(inorder)

        def dfs(preorder: deque[TreeNode], inorder: deque[TreeNode]):
            if len(used_val) >= n or inorder[0] in used_val:
                return None
            node_val = preorder.popleft()
            node = TreeNode(node_val)
            used_val.add(node_val)
            left, right = None, None
            if inorder[0] != node_val:
                left = dfs(preorder, inorder)
            if len(inorder) > 0 and inorder[0] == node_val:  # is leaf
                inorder.popleft()
                right = dfs(preorder, inorder)
            node.left, node.right = left, right
            return node
        root = dfs(p, i)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        solution: use idx
        '''
        n = len(inorder)
        p, i = 0, 0

        def dfs(bound: int):  # bound: the node val
            nonlocal p, i
            if p >= n or inorder[i] == bound:  # hit mid(parent)
                return None
            node = TreeNode(preorder[p])
            p += 1
            left = dfs(node.val)
            if i < n and node.val == inorder[i]:  # all left branch finished
                i += 1
            right = dfs(bound)
            node.left, node.right = left, right
            return node
        root = dfs(10000)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        solution:
        '''
        p, i = 0, 0
        n = len(preorder)

        def dfs(limit):
            nonlocal p, i
            if p >= n:
                return None
            if limit == inorder[i]:
                i += 1  # go to right branch
                return None
            node = TreeNode(preorder[p])
            p += 1
            left = dfs(node.val)
            right = dfs(limit)
            node.left, node.right = left, right
            return node
        # an near inf limit means a left only linear tree
        return dfs(10000)
