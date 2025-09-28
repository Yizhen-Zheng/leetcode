# Definition for a binary tree node.
import json
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
??? so simple???
7:15-7:56 42 min

why mid-order alone not work:

    2           
   / \
  1   3

  1
   \
    2
     \
      3

    3
   /
  2
 /
1  
all gives [N,1,N,2,N,3,N]
'''


class Codec:
    '''
    2 traversal
    '''

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return json.dumps(None)
        pre_order = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur is not None:
                pre_order.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)
            else:
                pre_order.append(None)
        return json.dumps({'pre': pre_order})

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree_data = json.loads(data)
        if not tree_data:
            return None

        pre_vals = tree_data['pre']

        def dfs(vals, idx):
            print(vals)
            if idx >= len(vals) or idx < 0:
                return None, idx
            if vals[idx] is not None:
                node = TreeNode(vals[idx])
                left, idx = dfs(vals, idx+1)
                right, idx = dfs(vals, idx+1)
                node.left, node.right = left, right
                return node, idx
            else:
                return None, idx
        root, _ = dfs(pre_vals, 0)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
