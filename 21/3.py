from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        edge case: eiher can be []
        [1]
        [100]
        [1, 4]
        [3]
        [1,2,4]
        [3, 5]
        '''
        def rec(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val < l2.val:
                l1.next = rec(l1.next, l2)
                return l1
            else:
                l2.next = rec(l1, l2.next)
                return l2

        return rec(list1, list2)
