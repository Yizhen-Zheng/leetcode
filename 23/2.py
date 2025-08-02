from typing import Optional
import heapq
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        reduce space using heap
        k:head num, n: individual list len
        t:O(k*n)
        s: O(k)
        '''
        count = 0  # dummy value to prevent heap err
        heap = []
        dummy = ListNode('dummy', None)
        cur = dummy
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, count, head))
            count += 1
        while heap:
            small = heapq.heappop(heap)[2]
            cur.next = small
            cur = cur.next
            if small.next:
                heapq.heappush(heap, (small.next.val, count, small.next))
            count += 1
        return dummy.next
