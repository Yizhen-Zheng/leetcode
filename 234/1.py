from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        brute-force: store val in an arr
        t:O(n)
        s:O(n)
        5min
        '''
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        n = len(arr)
        for l in range(n//2):
            if arr[l] != arr[-l-1]:
                return False
        return True

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        reverse the last half
        25min
        '''
        if head == None or head.next == None:
            return True

        tail = head
        count = 1
        mid = head
        while tail.next:
            count += 1
            tail = tail.next
            mid = mid.next
            if tail.next:
                tail = tail.next
                count += 1

        prev = None
        while mid:  # reverse the right half
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        for _ in range(count//2):
            if tail.val != head.val:
                return False
            tail = tail.next
            head = head.next
        return True

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        reverse the last half
        reverse origin back
        '''
        if head == None or head.next == None:
            return True

        tail = head
        mid = head
        while tail and tail.next:
            tail = tail.next.next  # after this, tail can be None if there're even nodes
            mid = mid.next
        prev = None
        while mid:  # reverse the right half
            # temp = mid.next
            # mid.next = prev
            # prev = mid
            # mid = temp
            mid.next, prev, mid = prev, mid, mid.next
        tail = prev
        carry_head, carry_tail = head, tail
        while tail:
            if tail.val != head.val:
                return False
            tail = tail.next
            head = head.next
        prev = None
        tail = carry_tail
        while tail:
            # temp = tail.next
            # tail.next = prev
            # prev = tail
            # tail = temp
            tail.next, prev, tail = prev, tail, tail.next
        while carry_head:
            print(carry_head.val)
            carry_head = carry_head.next
        return True
