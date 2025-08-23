
from typing import Optional
import heapq

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        brute force: seems heap(big root heap)
        but search tree(so only go left, if not enough value, turn right)
        in order (left, mid, right)
        14:48-14:52, not finished 
        22:54 - 23:01 
        10:39-10:45 
        17+min 
        t: O(k)(need visit k nodes)(worst case O(n))
        s:O(height)(worst case O(n))

        Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
        - add subtree_size to node's attribute
        when traversal, 
            if subtree_size > k, go left
            if subtree_size == k, return node
            if subtree_size < k, go right
        reduce runtime to O(logn)
        how reduces: no need to count from 0 to k(we can find kth node before 0th node)
        '''
        # if it's currently left and len(nodes)==k, return
        # nodes.append((-val,idx))
        def rec(node: TreeNode, idx: int):
            if not node:
                return idx, None
            idx, res = rec(node.left, idx)
            if idx == k:
                return idx, res
            idx += 1
            if idx == k:
                return k, node
            idx, res = rec(node.right, idx)
            if idx == k:
                return idx, res
            return idx, None
        _, res = rec(root, 0)
        return res.val

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        iterative
        7min
        t:O(k)
        s:O(n)(need store nodes from root, l, r )
        '''
        s = [(root, False)]
        count = 0
        while s:
            cur, visited = s.pop()
            if cur != None and visited:
                count += 1
                if count == k:
                    return cur.val
            elif cur != None:
                s.append((cur.right, False))
                s.append((cur, True))
                s.append((cur.left, False))
        return
