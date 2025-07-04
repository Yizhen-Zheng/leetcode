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
            smaller = list1
            greater = list2
        else:
            smaller = list2
            greater = list1

        head = smaller
        while smaller and greater:
            while smaller.next != None and smaller.next.val <= greater.val:
                # exit condition shoud be smaller.next.val <= greater.valif ,
                # so smaller can continue until find next None or greater
                smaller = smaller.next
            temp = smaller.next  # store next greater
            smaller.next = greater
            greater = temp

        return head
