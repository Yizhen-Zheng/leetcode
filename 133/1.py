
# Definition for a Node.
from typing import Optional

'''
graph traverse: 
t: O(N+E)
s: O(N)(lookup, and stack depth)
'''


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        '''
        brute force: use dict
        node is not a list! it's a single node
        25min
        t:O(E)
            traversal:O(n+edge number)
            copy:O(n+edge number)
        s:O(n)
            traversal: stack: O(n) (hold n nodes maximum)
            dict: O(n)
        '''
        if not node:
            return None
        origin_to_copy = {}
        s = [node]
        while s:
            cur_origin = s.pop()
            origin_to_copy[cur_origin] = Node(cur_origin.val)  # add new node
            for origin_neighbor in cur_origin.neighbors:
                if origin_neighbor not in origin_to_copy:
                    s.append(origin_neighbor)

        for origin in list(origin_to_copy.keys()):
            new = origin_to_copy[origin]
            for neighbor in origin.neighbors:
                new.neighbors.append(origin_to_copy[neighbor])

        return origin_to_copy[node]

    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        '''
        can i avoid duplicated traversal?
        add other properties on origin node
        33min
        t: O(E)
        s: O(n)
        '''
        if not node:
            return None
        s = [node]
        while s:
            cur_origin = s.pop()
            if not hasattr(cur_origin, 'copied'):
                cur_origin.copied = Node(cur_origin.val)  # add new node
                for origin_neighbor in cur_origin.neighbors:
                    if not hasattr(origin_neighbor, 'copied'):
                        s.append(origin_neighbor)
        # copy edges
        s = [node]

        while s:
            cur_origin = s.pop()
            if not hasattr(cur_origin, 'visited'):
                cur_origin.visited = True
                for neighbor in cur_origin.neighbors:
                    cur_origin.copied.neighbors.append(neighbor.copied)
                    if not hasattr(neighbor, 'visited'):
                        s.append(neighbor)

        new_node = node.copied
        s = [node]
        while s:
            cur_origin = s.pop()
            delattr(cur_origin, 'visited')
            delattr(cur_origin, 'copied')
            for neighbor in cur_origin.neighbors:
                if not hasattr(neighbor, 'visited'):
                    s.append(neighbor)
        return new_node

    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        '''
        DFS
        given Node.val is unique for each node, maybe i can just copy the val
        a dict, val to new copied
        maybe a hash arr can get in one run
        25min
        time: O(n+E)
        space:O(n)
        '''
        if not node:
            return None
        lookup = [None]*101
        s = [node]
        while s:
            origin = s.pop()
            idx = origin.val
            if not lookup[idx]:  # not copied yet
                copied = Node(origin.val)
                lookup[idx] = copied  # add new node
            else:
                copied = lookup[idx]
            if len(copied.neighbors) < 1:  # edges not copied yet
                for origin_neighbor in origin.neighbors:  # copy edges
                    neighbor_idx = origin_neighbor.val
                    if not lookup[neighbor_idx]:  # neighbor's copy not exist yet
                        lookup[neighbor_idx] = Node(origin_neighbor.val)  # create neighbor's copy
                    copied.neighbors.append(lookup[neighbor_idx])  # copy edges
                    copied_neighbor = lookup[neighbor_idx]
                    if len(copied_neighbor.neighbors) < 1:  # neighbor's copied has not processed edges yet
                        s.append(origin_neighbor)
        return lookup[node.val]

    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        '''
        BFS
        15min
        '''
        if not node:
            return None
        q = [node]
        origin_to_copy = {}
        idx = 0
        while idx < len(q):
            cur = q[idx]
            idx += 1
            if cur not in origin_to_copy:
                copied_cur = Node(cur.val)
                origin_to_copy[cur] = copied_cur
            else:
                copied_cur = origin_to_copy[cur]
            if len(copied_cur.neighbors) < 1:
                for neighbor in cur.neighbors:
                    if neighbor not in origin_to_copy:
                        origin_to_copy[neighbor] = Node(neighbor.val)
                    copied_cur.neighbors.append(origin_to_copy[neighbor])
                    if len(origin_to_copy[neighbor].neighbors) < 1:
                        q.append(neighbor)

        return origin_to_copy[node]

    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        '''try to simplify BFS'''
        if not node:
            return None
        q = [node]
        origin_to_copy = {node: Node(node.val)}
        idx = 0
        while idx < len(q):
            cur = q[idx]
            idx += 1
            copied_cur = origin_to_copy[cur]
            for neighbor in cur.neighbors:
                if neighbor not in origin_to_copy:
                    origin_to_copy[neighbor] = Node(neighbor.val)
                    q.append(neighbor)  # append first time seem, avoid duplicated enque
                    # (for the reson after first time we can ensure it is in the queue)
                copied_cur.neighbors.append(origin_to_copy[neighbor])
        return origin_to_copy[node]

    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        '''try to simplify BFS, use val as key'''
        if not node:
            return None
        q = [node]
        origin_to_copy = {node.val: Node(node.val)}
        idx = 0
        while idx < len(q):
            cur = q[idx]
            idx += 1
            copied_cur = origin_to_copy[cur.val]
            for neighbor in cur.neighbors:
                if neighbor.val not in origin_to_copy:
                    origin_to_copy[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)  # append first time seem, avoid duplicated enque
                    # (for the reson after first time we can ensure it is in the queue)
                copied_cur.neighbors.append(origin_to_copy[neighbor.val])
        return origin_to_copy[node.val]

    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        '''simplify DFS, use val as key'''
        if not node:
            return None
        stack = [node]
        origin_to_copy = {node.val: Node(node.val)}

        while stack:
            cur = stack.pop()
            copied_cur = origin_to_copy[cur.val]
            for neighbor in cur.neighbors:
                if neighbor.val not in origin_to_copy:
                    origin_to_copy[neighbor.val] = Node(neighbor.val)
                    stack.append(neighbor)  # append first time seem, avoid duplicated enque
                    # (for the reson after first time we can ensure it is in the queue)
                copied_cur.neighbors.append(origin_to_copy[neighbor.val])
        return origin_to_copy[node.val]

    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        '''
        rec, DFS
        15min
        '''
        if not node:
            return None
        origin_to_copy = {}

        def copy(origin: Node, origin_to_copy):
            if origin in origin_to_copy:
                return origin_to_copy[origin]
            copied_cur = Node(origin.val)
            origin_to_copy[origin] = copied_cur
            for neighbor in origin.neighbors:
                copied_neighbor = copy(neighbor, origin_to_copy)
                copied_cur.neighbors.append(copied_neighbor)
            return copied_cur
        return copy(node, origin_to_copy)

    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        '''rec, use val as key'''
        if not node:
            return None
        origin_to_copy = {}

        def copy(origin: Node, origin_to_copy):
            if origin.val in origin_to_copy:
                return origin_to_copy[origin.val]

            copied_cur = Node(origin.val)
            origin_to_copy[origin.val] = copied_cur
            for neighbor in origin.neighbors:
                copied_neighbor = copy(neighbor, origin_to_copy)
                copied_cur.neighbors.append(copied_neighbor)
            return copied_cur
        return copy(node, origin_to_copy)
