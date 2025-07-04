from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetweenI(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        first: find entry point
        Pre-calculate to Avoid Runtime Decisions
        try to imrpove without dummy
        '''
        if left == right or head.next == None:
            return head

        need_change_head = False
        if left == 1:
            need_change_head = True
        nodes = []
        current = head
        # start from 1, equivalent to (0, right+1)
        for _ in range(1, right+2):
            if current:
                nodes.append(current)
                current = current.next
            else:
                nodes.append(None)

        left_prev = nodes[left-2] if not need_change_head else None
        # nodes[right] if right's next
        prev = nodes[right]
        for i in range(left-1, right):
            nodes[i].next = prev
            prev = nodes[i]

        if left_prev:
            left_prev.next = prev
            return head
        return prev

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        first: find entry point
        try to imrpove without dummy
        '''
        if left == right or head.next == None:
            return head
        # move to left_prev:
        current = head
        left_prev = None
        for _ in range(left-1):
            left_prev = current
            current = current.next
        # current is left now
        prev = None
        left_node = current
        for _ in range(right-left+1):
            # connect back from left to right, include right(point to right-1)
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        # current is right+1 now
        left_node.next = current
        if left == 1:
            return prev
        # left_prev point to right
        left_prev.next = prev
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
