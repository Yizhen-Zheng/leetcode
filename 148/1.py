from typing import Optional
import random
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def visualize(head: ListNode):
    print()
    while head:
        print(head.val)
        head = head.next
    print()


def visualize_l(nodes: list[ListNode]):
    print()
    for node in nodes:
        print(node.val)
    print()


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        brute force: put into arr and sort, then reconnect
        quick sort:
        t:O(nlogn)
        t:O(n)
        45min TLE
        '''
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        def partition(nodes, start, end, pivot):
            i, j, ptr = start, end, start
            piv_val = nodes[pivot].val
            nodes[pivot], nodes[start] = nodes[start], nodes[pivot]
            while ptr <= j:  # cannot use i<j, since there may be many pivot values between i and j
                if nodes[ptr].val < piv_val:
                    nodes[ptr], nodes[i] = nodes[i], nodes[ptr]
                    ptr += 1
                    i += 1
                elif nodes[ptr].val == piv_val:
                    ptr += 1
                elif nodes[ptr].val > piv_val:
                    nodes[ptr], nodes[j] = nodes[j], nodes[ptr]
                    j -= 1
            return i-1, j+1
        stack = [(0, len(nodes)-1)]
        while stack:
            start, end = stack.pop()
            if start >= end:
                continue
            pivot_idx = random.randint(start, end)
            left_end, right_start = partition(nodes, start, end, pivot_idx)
            stack.append((start, left_end))
            stack.append((right_start, end))
        nodes.append(None)
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        return nodes[0]

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        quicksort on a list(in-place)
        LTE
        45min
        '''
        def partition(node: ListNode):
            piv_val = node.val
            left_start = right_start = left_end = right_end = None
            mid_start = mid_end = node
            while node:
                cur_node = node
                node = node.next
                if cur_node.val < piv_val:
                    if not left_start:
                        left_start = left_end = cur_node
                    else:
                        left_end.next = cur_node
                        left_end = cur_node
                elif cur_node.val == piv_val:
                    mid_end.next = cur_node
                    mid_end = cur_node
                elif cur_node.val > piv_val:
                    if not right_start:
                        right_start = right_end = cur_node
                    else:
                        right_end.next = cur_node
                        right_end = cur_node
            return left_start, left_end, mid_start, mid_end, right_start, right_end

        def rec(start_node):
            if not start_node or not start_node.next:
                return start_node, start_node

            left_start, left_end, mid_start, mid_end, right_start, right_end = partition(start_node)
            if left_start:  # partition produced left side(there're elems < piv)
                left_end.next = None
                new_left_start, new_left_end = rec(left_start)
            if right_start:  # partition produced right side(there're elems > piv)
                right_end.next = None
                new_right_start, new_right_end = rec(right_start)
            # reconnect parts
            head = tail = None
            if left_start:  # new_left_start and new_left_end exists
                head = new_left_start
                new_left_end.next = mid_start  # connect to mid
            else:
                head = mid_start
            if right_start:  # new_right_start and new_right_end exists
                tail = new_right_end
                mid_end.next = new_right_start  # connect to mid
            else:
                tail = mid_end
            tail.next = None
            return head, tail
        return rec(head)[0]

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        merge sort
        '''
        def split(start, unit_len):
            if not start:
                return None
            count = 1
            ptr = start
            while count < unit_len and ptr.next:
                count += 1
                ptr = ptr.next
            new_start = ptr.next if ptr.next else None
            ptr.next = None
            return new_start

        def merge(left_start: ListNode,  right_start: ListNode, prev_head: ListNode):
            prev = prev_head
            while left_start and right_start:
                if left_start.val <= right_start.val:
                    prev.next = left_start
                    left_start = left_start.next
                else:
                    prev.next = right_start
                    right_start = right_start.next
                prev = prev.next

            remain = left_start if left_start else right_start
            prev.next = remain
            while prev.next:
                prev = prev.next

            return prev

        node = head
        count_len = 0
        while node:
            count_len += 1
            node = node.next

        unit_len = 1
        left_start = right_start = None
        dummy = ListNode('dummy', head)

        # alternatively, use a dummy node as prev_end
        while unit_len < count_len:  # as least 2 nodes
            next_head = dummy.next
            prev_head = dummy
            while next_head:
                left_start = next_head
                right_start = split(left_start, unit_len)
                next_head = split(right_start, unit_len)
                # prev group's tail is next group's prev head
                prev_head = merge(left_start, right_start, prev_head)

            unit_len <<= 1

        return dummy.next


def make_test(nums):
    head = ListNode(nums[0])
    prev = head
    for num in nums[1:]:
        new_node = ListNode(num)
        prev.next = new_node
        prev = new_node
    return head


t = [-3]
t = [-3, 1, 0]
# t = [1, 6, 3, -3]
# t = [i for i in range(2, 50001)]+[1]
ll = make_test(t)
visualize(ll)
r = Solution().sortList(ll)
visualize(r)
