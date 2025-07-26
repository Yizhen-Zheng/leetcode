from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        hash table,
        3 min
        t: O(n)
        s: O(n)
        '''
        nodes = set()
        while head:
            if head in nodes:
                return True
            nodes.add(head)
            head = head.next
        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        2-ptr
        time O(1)
        s: O(1)
        8 min
        '''
        if (not head) or (not head.next) or (not head.next.next):
            return False
        slow, fast = head, head.next.next  # currently fast is not None
        while slow != fast and slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if not fast or not fast.next:
            return False
        return True


'''

'''
