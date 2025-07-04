from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        with dummy
        why this if much faster
        Less memory overhead from extra variables
        Fewer CPU instructions
        The dummy node creates a more linear memory access pattern. 
        Without it, you're doing more pointer chasing and conditional jumps, which can hurt CPU cache performance.
        '''
        dummy = ListNode('dummy', head)
        current = dummy
        idx = 0

        while idx < left-1:  # when current's next is not left
            current = current.next
            idx += 1
        # current: left - 1
        left_prev = current
        next = current.next
        # start reverse
        while idx < right:
            temp = next.next
            next.next = current
            current = next
            next = temp
            idx += 1

        # at this time current is pointing to right's next
        left_prev.next.next = next
        left_prev.next = current

        return dummy.next


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


# t = factory(6)
# r = Solution().reverseBetween(t, 2, 4)
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
t = factory(3)
r = Solution().reverseBetween(t, 2, 3)
show(r)
