from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        k>=nodes(len)
        use a container
        45min 
        time: O(n)
        space: O(n)
        '''
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        n = len(nodes)
        for i in range(k-1, n, k):
            new_head = nodes[i]
            next_idx = i-1
            while next_idx > i-k:
                new_head.next = nodes[next_idx]
                new_head = new_head.next
                next_idx -= 1
            next_idx = i+k
            if i+k > n-1:
                next_idx = i+1
            new_head.next = nodes[next_idx] if next_idx < n else None
        return nodes[k-1]

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        try not use a container
        difficult is we don't know if current working one is valid or not have enough k nodes
        option1: use container to count if remaining nodes are more than k (15 min)
        option2: reverse them back if find less than k 
        time: O(n)
        space: O(k)
        '''
        head_of_all = None
        prev_tail = None  # tail of last group to connect

        while head:
            cur_group = []
            for _ in range(k):
                if not head:  # no enough node ramaining
                    break
                cur_group.append(head)
                head = head.next  # now head is in next group
            n = len(cur_group)
            if n < k:  # end of list, no enough nodes
                prev_tail.next = cur_group[0]
                break
            elif prev_tail:
                prev_tail.next = cur_group[-1]  # connect prev group with cur

            if not head_of_all:  # assign new head to return
                head_of_all = cur_group[-1]
            prev_tail = cur_group[0]
            prev = None
            cur = cur_group[0]
            for _ in range(n):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
        return head_of_all

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        realized no need to keep an arr, just record head and tail
        time: O(n)
        space: O(1)
        '''
        head_of_all = None
        prev_tail = None  # tail of last group to connect

        while head:
            group_head = None  # 1st elem in origin order
            group_tail = None  # last elem in origin order
            count = 0
            for _ in range(k):
                if not head:  # no enough node ramaining
                    break
                count += 1
                if not group_head:
                    group_head = head
                group_tail = head  # update last elemend record in current group
                head = head.next  # now head is in next group

            if count < k:  # end of list, no enough nodes
                prev_tail.next = group_head
                break
            elif prev_tail:
                prev_tail.next = group_tail  # connect prev group with cur

            if not head_of_all:  # assign new head to return
                head_of_all = group_tail
            prev_tail = group_head
            prev = None
            cur = group_head
            for _ in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
        return head_of_all
