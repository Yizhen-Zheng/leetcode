from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        have 2 parts: smaller, greater, keep watch themselves' head and tail, reconnect at the end
        need to ensure greater's tail is None, otherwise will make a circle and time limit exceed
        either use a temp to reserve current's next, clear tail every iteration
        or clear tail at finish
        '''
        cur = head
        greater_head = None
        greater_tail = None
        smaller_head = None
        smaller_tail = None

        while cur:
            if cur.val < x:
                if not smaller_head:
                    smaller_head = cur
                else:
                    smaller_tail.next = cur
                smaller_tail = cur

            else:
                if not greater_head:
                    greater_head = cur
                else:
                    greater_tail.next = cur
                greater_tail = cur
            cur = cur.next

        if greater_tail:
            # same as set cur.next = None and use temp as next
            greater_tail.next = None
        if smaller_tail:
            smaller_tail.next = greater_head
            return smaller_head
        return greater_head
