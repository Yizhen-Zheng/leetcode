from typing import List
import heapq
from collections import deque
'''
review heap:
why bottom down is faster:
bottom up: generally O(n)
    elements: from last second layer, back to 0
    approach: heapify_down
    for every elem, try to swap it with its children
    so the last layer need swap most 1 times, 
    the higher layer with less elems need to swap more times
top down:
    elems: from 0 to last elem
    approach: heapify_up
    for every elem, try to swap it with its parent
    for nums[0], swap 0 times
    for lower layer(with more elems), need to swap more times with higher ones

'''


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        '''
        push negative into heapq
        it's the heapq that compares elem by elem[0],elem[1]...
        time: 
            O(nlogn)
            form heap: O(nlogn)
                heappush: logn, push n nums
            reduce: O(n)(worst case: [1,1,1,1], reduce 4 times)

        '''

        max_heap = []
        cur_sum = 0
        for num in nums:
            heapq.heappush(max_heap, -num)
            cur_sum += num
        half = cur_sum/2
        count = 0
        while cur_sum > half:
            cur_num_half = (heapq.heappop(max_heap))/2
            cur_sum += cur_num_half
            heapq.heappush(max_heap, cur_num_half)
            count += 1
        return count

    def halveArray(self, nums: List[int]) -> int:
        '''
        deque
        edge case:
        [1,1,1,1]: need to pop origin until empty, then finish at the same time
        [100]: pop one time, then finish 
        [3,2]: pop until empty, then finish
        worst case: half all once([1,1,1]), empty the origin, but exit immediately
        which guarantee not reach the pop empty origin
        (we can always expect we'll reuse the larger number, or use each number exactly one time)
        '''
        nums.sort(reverse=True)
        origin_nums = deque(nums)
        halfed = deque()
        target = sum(nums)/2
        cur_sum = 0
        count = 0
        while cur_sum < target:
            if not halfed or halfed[0] < origin_nums[0]:
                num = origin_nums.popleft()/2
            else:
                num = halfed.popleft()/2
            cur_sum += num
            halfed.append(num)
            count += 1
        return count


t = []
t = [0]
t = [0, 1]
t = [2, 5, 1]
r = Solution().halveArray(t)
print(r)
