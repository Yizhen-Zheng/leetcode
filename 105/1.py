

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        '''
        17:04-17:59
        root: preorder[0]
        left_most:inorder[0]
        values are unique
        not balanced
        t: O(n * logn) average, worst case O(n*n)(a linear tree on left),best O(1)(a linear tree on right)
        s: O(n) average, O(n) worst case(a linear tree no matter on left or right),
        '''

        def rec(preo_iter: iter, inorder: list[int]):
            print(inorder)
            if len(inorder) == 0:  # current node is (None)
                return None  # proof we're not mistakenly using iter

            parent_val = next(preo_iter)
            parent = TreeNode(parent_val)
            inorder_parent_idx = inorder.index(parent_val)  # O(m)(m: )
            print(inorder_parent_idx)

            left_child = rec(preo_iter, inorder[:inorder_parent_idx])
            parent.left = left_child

            right_child = rec(preo_iter, inorder[inorder_parent_idx+1:])
            parent.right = right_child

            return parent

        preo_iter = iter(preorder)
        root = rec(preo_iter, inorder)
        return root

    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        '''
        stack version
        11:00-11:23, 23min
        '''
        root = TreeNode(preorder[0])
        root_pos = inorder.index(preorder[0])  # first mid point
        m = len(preorder)
        s = [(root_pos+1, m,  root, 'r'), (0, root_pos-1, root, 'l')]  # [lo,hi,parent,'l or r'], lo and hi are included
        pre_idx = 1  # start from next after root
        while pre_idx < m:
            lo, hi, parent, lr = s.pop()
            if lo > hi:
                continue
            val = preorder[pre_idx]
            pre_idx += 1
            node = TreeNode(val)
            if lr == 'l':
                parent.left = node
            elif lr == 'r':
                parent.right = node
            mid = inorder.index(val)
            l_child = (lo, mid-1, node, 'l')
            r_child = (mid+1, hi, node, 'r')
            s.append(r_child)
            s.append(l_child)
        return root

    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        '''
        stack version
        MAKE HASHMAP to quickly check idx!!!
        t: O(n)
        s: O(n)(hashtable, and worst for linear tree)
        '''
        m = len(preorder)
        val_to_in = {}
        for i in range(m):
            node_val = inorder[i]
            val_to_in[node_val] = i

        root = TreeNode(preorder[0])
        root_pos = val_to_in[preorder[0]]  # first mid point
        s = [(root_pos+1, m,  root, 'r'), (0, root_pos-1, root, 'l')]  # [lo,hi,parent,'l or r'], lo and hi are included
        pre_idx = 1  # start from next after root
        while pre_idx < m:
            lo, hi, parent, lr = s.pop()
            if lo > hi:
                continue
            val = preorder[pre_idx]
            pre_idx += 1
            node = TreeNode(val)
            if lr == 'l':
                parent.left = node
            elif lr == 'r':
                parent.right = node
            mid = val_to_in[val]
            l_child = (lo, mid-1, node, 'l')
            r_child = (mid+1, hi, node, 'r')
            s.append(r_child)
            s.append(l_child)
        return root

    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        '''
        without hashmap
        t: O(n)
        s: O(height)
        '''
        def rec(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = rec(root.val)
                inorder.pop()  # left part finished,remove
                root.right = rec(stop)
                return root

        preorder = reversed(preorder)
        inorder = reversed(inorder)
        root = rec(None)
        return root

    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        '''try evolve to above'''
        n = len(preorder)
        val_to_idx = {}
        for i in range(n):
            val_to_idx[inorder[i]] = i

        def rec(pre_iter, lo, hi):
            if lo <= hi:
                val = next(pre_iter)
                node = TreeNode(val)
                mid = val_to_idx[val]
                left = rec(pre_iter, lo, mid-1)
                right = rec(pre_iter, mid+1, hi)
                node.left = left
                node.right = right
                return node
        root = rec(iter(preorder), 0, n-1)
        return root

    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        '''
        try evolve to no map version
        stop: hi
        remove first of inoder after finishing left, so they can maintain order 
        for single node like[1], the rec will be:
        stop=None
        l: stop=1, inorder[-1]==1, return
        r: stop=None, inorder=[], return
        '''
        n = len(preorder)
        preorder = list(reversed(preorder))
        inorder = list(reversed(inorder))

        def rec(stop):
            if inorder and inorder[-1] != stop:
                val = preorder.pop()
                node = TreeNode(val)

                left = rec(val)  # lo,mid-1
                # remove itself from inorder
                inorder.pop()
                right = rec(stop)  # mid+1, hi
                node.left = left
                node.right = right
                return node
        root = rec(None)  # 0 - n-1
        return root


t = ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
r = Solution().buildTree(t[0], t[1])
print(r)
