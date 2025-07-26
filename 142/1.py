from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''brute force, space: O(n)'''
        nodes = set()
        while head:
            if head in nodes:
                return head
            nodes.add(head)
            head = head.next
        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        2ptr
        25min
        time: O(n)
        space: O(1)
        NOTE that either slow and fast both start from 0(dummy) and start count, 
        or both start from 1(head), and initially have one step(slow: head.next), fast:(head.next.next)
        a usual mismatch i made: slow=1(head, which haven't moved yet), and fast=head.next.next(already moved )
        '''
        if not head or not head.next or not head.next.next:
            return None
        dummy = ListNode('dummy')
        dummy.next = head
        slow, fast = head, dummy.next.next
        while slow != fast and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if not fast or not fast.next:
            return None

        slow = dummy
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        2ptr
        time: O(n)
        space: O(1)
        without dummy

        '''
        if not head or not head.next or not head.next.next:
            return None
        slow, fast = head.next, head.next.next
        while slow != fast and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if not fast or not fast.next:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        2ptr
        time: O(n)
        space: O(1)
        without dummy, start at 0

        '''
        if not head or not head.next or not head.next.next:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
