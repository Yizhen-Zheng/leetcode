from typing import Optional
# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        '''
        container, store all in the first traverse, 
        then move the random pointer to the copied nodes
        the problem is to store the address of new random pointer
        copy the random pointer first
        45min
        time: O(n)
        space: O(n)
        '''

        nodes = []
        origin_nodes = {}  # {origin_id:new_idx}
        while head:
            new_head = Node(head.val, head.next, head.random)
            origin_id = id(head)
            origin_nodes[origin_id] = len(nodes)
            nodes.append(new_head)
            head = head.next
        n = len(nodes)
        nodes.append(None)  # handle tail

        for i in range(n):
            cur_node = nodes[i]
            cur_node.next = nodes[i+1]  # move next pointer to new copied node

            origin_target = cur_node.random
            if origin_target:  # if random pointer is not None
                origin_id = id(origin_target)
                idx = origin_nodes[origin_id]
                cur_node.random = nodes[idx]
        return nodes[0]

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        '''
        container, store all in the first traverse, 
        we can directly store node as dict key without getting its id
        time: O(n)
        space: O(n)
        '''

        nodes = []
        origin_nodes = {}  # {origin_id:new_idx}
        while head:
            new_head = Node(head.val, head.next, head.random)
            origin_nodes[head] = len(nodes)
            nodes.append(new_head)
            head = head.next
        n = len(nodes)
        nodes.append(None)  # handle tail
        for i in range(n):
            cur_node = nodes[i]
            cur_node.next = nodes[i+1]  # move next pointer to new copied node

            origin_target = cur_node.random
            if origin_target:  # if random pointer is not None
                idx = origin_nodes[origin_target]
                cur_node.random = nodes[idx]
        return nodes[0]

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        '''
        container, store origin in dict key, store new nodes in corresponding val
        time: O(n)
        space: O(n)
        15 min, check the solution
        '''
        if not head:
            return None
        nodes = {}
        origin_node = head
        while origin_node:  # add to dict
            nodes[origin_node] = Node(origin_node.val)
            origin_node = origin_node.next
        key = head
        while key:
            next_key = key.next
            random_key = key.random
            nodes[key].next = nodes[next_key] if next_key else None  # move new nodes' next pointer
            nodes[key].random = nodes[random_key] if random_key else None
            key = key.next
        return nodes[head]

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        '''
        A->A'->B->B'...
        time: O(n)
        space: O(1)(?)

        '''
        if not head:
            return None
        origin_node = head
        while origin_node:  # reconnect (insert new node into origin)
            new_node = Node(origin_node.val, origin_node.next)
            origin_node.next = new_node
            origin_node = new_node.next

        origin_node = head
        new_head = head.next

        while origin_node:
            new_node = origin_node.next
            random_ptr = origin_node.random
            new_node.random = random_ptr.next if random_ptr else None  # move new nodes' next pointer
            origin_node = new_node.next

        # remove from origin LL
        origin_node = head
        while origin_node:
            new_node = origin_node.next
            origin_node.next = new_node.next  # move origin's next ptr to next origin(skip new)
            origin_node = origin_node.next  # move origin ptr to next origin
            new_node.next = new_node.next.next if new_node.next else None  # move new node's next ptr to next new

        return new_head
