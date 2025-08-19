# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        8:50-9:07 17min got it!
        t: O(n)
        s: O(n)
        brute force: 
        for every node, ask if the node is ancestor of target node(n^2)
        looks mid order traverse
        LL like, store path, pop until find diverge point(must have root as ancestor)
        node.val unique, seems good
        '''
        def dfs(node: TreeNode, target: TreeNode, path: list):
            if node == target:
                path.append(node)
                return path
            if not node:
                return None
            path_a = dfs(node.left, target, path)
            path_b = dfs(node.right, target, path)
            if path_a:
                path_a.append(node)
                return path_a
            elif path_b:
                path_b.append(node)
                return path_b
            print('nothing found')
            return None
        path_p = dfs(root, p, [])
        path_q = dfs(root, q, [])
        ancestor = root
        while path_p and path_q:
            ap, aq = path_p.pop(), path_q.pop()
            if ap != aq:
                return ancestor
            ancestor = ap
        return ancestor

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        try reduce space
        [hasp,hasq,node_found]
        9:30-9:54, not finished
        no pruning version
        no need to let child know if parent has 
        t:O(n)
        s:O(n), average:O(logn)
        '''
        def dfs(node: TreeNode, p: TreeNode, q: TreeNode):
            has_p, has_q = False, False
            if node == p:
                has_p = True
            if node == q:
                has_q = True
            if not node:
                return (has_p, has_q, None)
            # # should get conclusion AFTER traverse, to prove return ancestor instead of child
            # if has_p and has_q:
                # return (has_p, has_q, node)
            # so far: nothing found both has p and q
            l_has_p, l_has_q, l_node_found = dfs(node.left, p, q)
            if l_has_p and l_has_q:  # l has both p and q
                return (True, True, l_node_found)
            r_has_p, r_has_q, r_node_found = dfs(node.right, p, q)
            if r_has_p and r_has_q:  # r has both p and q
                return (True, True, r_node_found)

            if (l_has_p or r_has_p or has_p) and (l_has_q or r_has_q or has_q):  # try include cur
                return (True, True, node)
            return (l_has_p or r_has_p or has_p, l_has_q or r_has_q or has_q, None)

        _, _, ancestor = dfs(root, p, q)
        return ancestor

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        solution, simple
        if p is q's parent, we get p directly
        if p and q are not in same branch, they'll be returned from different rec branches
        '''
        def dfs(node: TreeNode, p: TreeNode, q: TreeNode):
            # this also handles p is q's parent
            if not node or node == q or node == p:
                return node
            l = dfs(node.left, p, q)
            r = dfs(node.right, p, q)

            # if cur found p,q in different branches, cur is LCA
            if l and r:
                return node

            # cur only contains one of p,q, and that one is not cur:
            return l or r
        return dfs(root, p, q)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        from constrains, p and q exist, and at least 2 nodes in the tree, 
        so seems p and q are not None
        '''
        s = [root]
        parent = {root: None}  # child -> parent
        while p not in parent or q not in parent:  # keep until find q and p
            node = s.pop()
            if node.left:
                parent[node.left] = node
                s.append(node.left)
            if node.right:
                parent[node.right] = node
                s.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]  # trace until root
        while q not in ancestors:
            q = parent[q]  # get upper until find
        return q

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = deque([root])
        parent = {root: None}
        while not (q in parent and p in parent):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                parent[node.left] = node
            if node.right:
                queue.append(node.right)
                parent[node.right] = node
        # finished traverse: find p and q
        p_parent = set()
        while p:  # trace p's parent until root
            p_parent.add(p)
            p = parent[p]
        while q not in p_parent:
            # if q higher than p, this loop won't be executed
            # otherwise, loop exits when reach 'joint'
            q = parent[q]
        return q
