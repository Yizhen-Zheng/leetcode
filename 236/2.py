# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        42 min
        5:25-5:42 17
        5:55-6:20 25

        '''
        p_path, q_path = [], []

        def find(node: TreeNode, target: TreeNode, path: list[int]):
            if not node:  # not find in this path
                return False
            if node == target:  # find
                path.append(node)
                return True
            find_l, find_r = find(node.left, target, path), find(node.right, target, path)
            if find_l or find_r:
                path.append(node)
                return True
            return False
        find(root, p, p_path)
        find(root, q, q_path)
        if len(q_path) > len(p_path):  # make sure p path is longer
            p_path, q_path = q_path, p_path
            p, q = q, p
        # iter from root
        p_ptr, q_ptr = len(p_path)-1, len(q_path)-1
        print(p_path)
        print(q_path)
        while p_ptr > -1 and q_ptr > -1:
            if p_path[p_ptr] == q:
                return q
            if p_path[p_ptr] != q_path[q_ptr]:
                break
            p_ptr -= 1
            q_ptr -= 1
        return p_path[p_ptr+1]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Solution:
        this covers the case where q or p is lca, 
        so it's safe to return whatever found once node == p or q
        '''
        def dfs(node: TreeNode):
            if node is None:
                return None
            if node is p or node is q:
                return node
            l_find, r_find = dfs(node.left), dfs(node.right)
            if l_find is not None and r_find is not None:  # the 2 lca merged at cur node
                return node
            return l_find or r_find
        lca = dfs(root)
        return lca
