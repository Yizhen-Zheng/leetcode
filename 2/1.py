
from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        val = (l1.val+l2.val)
        prev_digit = val//10
        l1.val = val % 10
        prev_node = l1
        cur1 = l1.next
        cur2 = l2.next
        while cur1 and cur2:
            val = cur1.val+cur2.val+prev_digit
            cur1.val = val % 10
            prev_digit = val//10
            prev_node = cur1
            cur1 = cur1.next
            cur2 = cur2.next

        if cur1 or cur2:
            cur = cur1 if cur1 else cur2
            prev_node.next = cur
            while cur:
                val = cur.val+prev_digit
                prev_digit = val//10
                cur.val = val % 10
                prev_node = cur
                cur = cur.next

        if prev_digit:
            prev_node.next = ListNode(prev_digit, None)

        return l1
