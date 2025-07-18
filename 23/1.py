from typing import List, Optional
import heapq
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        brute-force:
            1, k pointers, append the smallest one 
            2, traverse one by one and append number to a list, sort the list, and create new merged LL
        this is a bit cheat
        sort: nlogn
        traverse, reconnect: n
        total: time: O(nlogn), space: O(n)(total number of nodes)
        '''
        nums = []
        for head in lists:
            while head:
                nums.append(head.val)  # None will be appended if value is None
                head = head.next
        if not nums:
            return None
        nums.sort()
        dummy = ListNode('dummy', None)
        current_head = dummy
        for n in nums:
            new_node = ListNode(n, None)
            current_head.next = new_node
            current_head = current_head.next
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        heap:
        similar as brute force, but manually maintain the order
        time: (O(nlogn)), for every push requires heap up, and no repeated 2*n since only on time connect
        !!!space:  O(k), is better, and totally it's smarter
        (only k heads in the heap at the same time) 
        [[]], [None]: is not considered empty
        '''

        # heapq.heapify((head.val, head) for head in lists)
        c = 0
        q = []
        for node in lists:
            # this filter out both the empty backet and empty head([[]], [])
            if node:
                heapq.heappush(q, (node.val, c, node))
            c += 1
        dummy = ListNode('dummy', None)
        cur_node = dummy
        while q:
            val, _, node = heapq.heappop(q)
            cur_node.next = node
            cur_node = cur_node.next  # cur is the last valid elem in q
            if node.next:  # only push not None elem into q
                heapq.heappush(q, (node.next.val, c, node.next))
            c += 1
        return dummy.next
