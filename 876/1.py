from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        s-f ptr
        10min
        '''
        if not head:
            return None
        slow, fast = head, head.next
        while fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                break
            fast = fast.next
        return slow

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        s-f ptr
        NOTE we can manually make it mismatch one position and reduce the if condition for even nodes
        (make slow move one more step than fast comparing with they both starts from 0)
        '''
        if not head:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
