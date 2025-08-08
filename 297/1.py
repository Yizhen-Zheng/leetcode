from collections import deque
import json
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    '''
    38min, use json
    '''

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        dfs
        """

        def dfs(root: TreeNode):
            if not root:
                return {}
            d = {}
            d['val'] = root.val
            d['left'] = dfs(root.left)
            d['right'] = dfs(root.right)
            return d
        ans = dfs(root)
        str_ans = json.dumps(ans)
        return str_ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        dfs
        """
        d = json.loads(data)

        def dfs(d):
            if not d:
                return None
            root = TreeNode(d['val'])
            left = dfs(d['left'])
            right = dfs(d['right'])
            root.left = left
            root.right = right
            return root
        root = dfs(d)
        return root


class Codec:
    '''
    follow tutorial
    use DFS, track pos in arr, preorder
    45min
    '''

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        Note that it's dfs order, so no need to deal with layer count

        """
        ans = []

        def dfs(root: TreeNode, ans):
            if not root:
                ans.append('None')
                return
            ans.append(str(root.val))
            dfs(root.left, ans)
            dfs(root.right, ans)
            return
        dfs(root, ans)
        str_ans = ','.join(ans)
        print(str_ans)
        return str_ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode

        """
        arr = data.split(',')
        print(arr)
        n = len(arr)

        def dfs(pos, arr):
            '''
            return next pos to go
            '''
            # if pos > n-1 or pos < 0:
            if pos > n-1:  # both works, since only right most None will get -1
                return None, -1
            if arr[pos] == 'None':
                return None, pos+1
            val = arr[pos]
            cur = TreeNode(int(val))
            pos += 1
            left, pos = dfs(pos, arr)
            right, pos = dfs(pos, arr)
            cur.left = left
            cur.right = right
            return cur, pos
        root = dfs(0, arr)[0]
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        use iter instead of manually pass position
        """
        arr = data.split(',')
        print(arr)

        def dfs(vals):
            '''
            return next pos to go
            '''
            cur = next(vals)
            if cur == 'None':
                return None
            cur = TreeNode(int(cur))
            left = dfs(vals)
            right = dfs(vals)
            cur.left = left
            cur.right = right
            return cur
        vals = iter(arr)
        root = dfs(vals)[0]
        return root


class Codec:
    '''
    try DFS
    '''

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = []
        q = deque([root])
        while q:
            cur = q.popleft()
            if not cur:
                ans.append('None')
            else:
                ans.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right)
        str_ans = ','.join(ans)

        return str_ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        by appending correct child to corresponding position, 
        preven the mismatch(e,g,left is null and have deep right branches)
        """
        arr = data.split(',')
        if arr[0] == 'None':
            return None
        root = TreeNode(int(arr[0]))
        q = deque([root])
        pos = 1
        while q:
            cur = q.popleft()
            # process l
            if arr[pos] != 'None':
                left = TreeNode(int(arr[pos]))
                cur.left = left
                q.append(left)
            pos += 1
            # process r
            if arr[pos] != 'None':
                right = TreeNode(int(arr[pos]))
                cur.right = right
                q.append(right)
            pos += 1
        return root


class Codec:
    '''
    stack DFS
    '''

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        Note that it's dfs order, so no need to deal with layer count
        pre-order traverse
        """
        ans = []
        s = [root]
        while s:
            cur = s.pop()
            if not cur:
                ans.append('None')
            else:
                ans.append(str(cur.val))
                s.append(cur.right)
                s.append(cur.left)
        str_ans = ','.join(ans)
        print(str_ans)
        return str_ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        DFS
        for every node, first explore left until nothing, then shift to nearest right, 
        then explore l untile None...
        """
        print(data)
        # vals = iter(data.split(','))
        vals = data.split(',')
        n = len(vals)
        if n < 2:
            return None
        parent = root = TreeNode(int(vals[0]))
        s = [root]
        pos = 1
        while pos < n:
            while pos < n and vals[pos] != 'None':
                # left must end with None
                parent.left = TreeNode(int(vals[pos]))
                parent = parent.left
                s.append(parent)
                pos += 1

            # switch to Nones that below and adj to left leaf
            # until find nearest right
            while pos < n and vals[pos] == 'None':
                parent = s.pop()
                pos += 1

            # find right, use cur as parent and go left branch again
            if pos < n and vals[pos] != 'None':
                parent.right = TreeNode(int(vals[pos]))
                parent = parent.right
                s.append(parent)
                pos += 1
        return root

    def deserialize(self, data):
        '''
        DFS stack, with mark visited
        '''
        print(data)
        # vals = iter(data.split(','))
        vals = data.split(',')
        n = len(vals)
        if n < 2:
            return None
        root = TreeNode(int(vals[0]))
        s = [root]
        parent = s[-1]
        parent.l = False
        pos = 1
        while pos < n:
            parent = s.pop()
            if parent.l == False:  # go left
                s.append(parent)
                parent.l = True
                if vals[pos] != 'None':
                    l_child = TreeNode(int(vals[pos]))
                    parent.left = l_child
                    l_child.l = False
                    s.append(l_child)
            else:  # go right
                delattr(parent, 'l')
                if vals[pos] != 'None':
                    r_child = TreeNode(int(vals[pos]))
                    parent.right = r_child
                    r_child.l = False
                    s.append(r_child)
            pos += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
