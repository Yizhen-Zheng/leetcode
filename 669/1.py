from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        '''
        7:52-8:31
        find, keep right of low, keep left of high 
        assume low and high are not necessarily in the tree
        '''
        def find_low(node: TreeNode):
            '''
            find left most valid node
            '''
            if not node:
                return None
            if node.val == low:
                return node
            if node.val > low:  # low boundary in left
                l = find_low(node.left)
                if not l and node.val < high:  # cur is the valid smallest
                    return node
                return l  # might be None or node
            else:  # node.val<low: search bigger side
                return find_low(node.right)

        def find_high(node: TreeNode):
            if not node:
                return None
            if node.val == high:
                return node
            if node.val > high:
                return find_high(node.left)
            else:  # node.val<high:
                r = find_high(node.right)
                if not r and node.val > low:
                    return node
                return r
        low_node, high_node = find_low(root), find_high(root)
        if low_node is None and high_node is None:
            return None  # no node in range
        low_node.left, high_node.right = None, None

        def find_lca(node: TreeNode):
            if not node:
                return None

    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        '''
        omg works, unbelieveable...
        9:04~9:28 24min
        total: 39 + 24 = 63min

        '''
        def trim_low(node: TreeNode):
            '''
            find left most valid node
            '''
            if not node:
                return None
            if low <= node.val:  # valid node, trim left(currently consider right all valid)
                l = trim_low(node.left)
                node.left = l  # replace with trimed
                return node
            else:  # node.val<low: search bigger side
                return trim_low(node.right)  # will replace original l with valid right node(if any)

        def trim_high(node: TreeNode):
            if not node:
                return None
            if node.val <= high:
                r = trim_high(node.right)
                node.right = r
                return node
            else:  # node.val>high:
                return trim_high(node.left)

        return trim_high(trim_low(root))

    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        '''
        trim low and high
        '''
        def trim(node: TreeNode):
            '''
            find valid node
            '''
            if not node:
                return None
            if low <= node.val <= high:  # valid node, keep
                l = trim(node.left)
                r = trim(node.right)
                node.left, node.right = l, r  # replace with trimed
                return node
            elif node.val > high:  # too big, search smaller side
                return trim(node.left)
            else:  # too small
                return trim(node.right)

        return trim(root)
