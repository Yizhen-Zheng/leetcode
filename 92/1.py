from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        first: find entry point
        note that left, right is idx+1
        '''
        left_prev = None
        current = head
        count_idx = 1  # start from position 1

        while count_idx < left:  # when current is not left yet
            print(left_prev.val if left_prev else left_prev, '->', current.val)
            left_prev = current
            current = current.next
            count_idx += 1
        # currently:
        # left_prev is the prev node of left(which we want to reverse first), which is reserved in memory
        # idx is left

        left = current  # reserve this for latter connection
        prev = None
        next = None
        # start reverse
        while count_idx < right+1:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count_idx += 1

        # at this time current is pointing to right's next
        if current:  # if right is not the last node, connect origin left to origin right's next node
            left.next = current
        if left_prev:  # if origin left is not the first node, connect origin left's prev to origin right
            left_prev.next = prev
            # left_prev.next = current
        else:  # if origin left is head, change head to origin right
            head = prev
        return head


def factory(n):
    head = ListNode(1, None)
    cur = head
    for i in range(2, n+1):
        new_node = ListNode(i, None)
        cur.next = new_node
        cur = new_node
    return head


def show(head):
    path = []
    while head:
        path.append(head.val)
        path.append('->')
        head = head.next
    path.append(None)
    print(' '.join(map(str, path)))


t = factory(6)
r = Solution().reverseBetween(t, 2, 4)
# t = factory(2)
# r = Solution().reverseBetween(t, 1, 2)
# t = factory(1)
# r = Solution().reverseBetween(t, 1, 1)
# t = factory(3)
# r = Solution().reverseBetween(t, 1, 1)
# t = factory(3)
# r = Solution().reverseBetween(t, 1, 2)
# t = factory(3)
# r = Solution().reverseBetween(t, 3, 3)
# t = factory(3)
# r = Solution().reverseBetween(t, 2, 3)
show(r)
