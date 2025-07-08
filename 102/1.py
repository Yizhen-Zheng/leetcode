from typing import Optional, List
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderI(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        version1: list
        '''
        if not root:
            return []
        parent_layer = [root]
        res = []

        while parent_layer:
            parent_layer_val = []
            idx = 0
            children_layer = []
            while idx < len(parent_layer):
                node = parent_layer[idx]
                parent_layer_val.append(node.val)
                if node.left:
                    children_layer.append(node.left)
                if node.right:
                    children_layer.append(node.right)
                idx += 1
            res.append(parent_layer_val)
            parent_layer = children_layer
        return res

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        version2: deque, seems it's slow
        '''
        if not root:
            return []
        parent_layer = deque([root])
        res = []

        while parent_layer:
            parent_layer_val = []  # the list in result
            children_layer = []  # initialize a new children layer to store nodes in payer order
            while parent_layer:
                node = parent_layer.popleft()
                parent_layer_val.append(node.val)
                if node.left:
                    children_layer.append(node.left)
                if node.right:
                    children_layer.append(node.right)
            res.append(parent_layer_val)  # after traverse parent layer and get their value, put result
            parent_layer = deque(children_layer)  # change to next layer(which we've prepared when traverse parents)
        return res

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        version2: deque, seems it's slow
        '''
        if not root:
            return []
        res = [[root.val]]
        current_layer = [root]
        while current_layer:
            next_layer = []
            next_layer_val = []
            idx = 0
            while idx < len(current_layer):
                node = current_layer[idx]
                left, right = node.left, node.right
                if left:
                    next_layer.append(left)
                    next_layer_val.append(left.val)

                if right:
                    next_layer.append(right)
                    next_layer_val.append(right.val)

                idx += 1
            if next_layer_val:
                res += [next_layer_val]
            current_layer = next_layer
        return res
