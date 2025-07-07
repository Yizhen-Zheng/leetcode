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
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            cur1 = list1
            cur2 = list2
        else:
            cur1 = list2
            cur2 = list1

        head = cur1
        pre = cur1
        cur1 = cur1.next
        while cur1 and cur2:
            if cur1.val < cur2.val:
                pre.next = cur1
                cur1 = cur1.next
            else:
                pre.next = cur2
                cur2 = cur2.next
            pre = pre.next
        if cur1:
            pre.next = cur1
        elif cur2:
            pre.next = cur2
        return head
