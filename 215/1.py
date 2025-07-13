from typing import List
import random
'''
for loop idx can be negative
    for i in range(-1,-4,-1):
        print(i)
    -1
    -2
    -3
'''


class Solution:
    def findKthLargestI(self, nums: List[int], k: int) -> int:
        # ???it works, unbelievable
        '''
        Hash solution:
        cannot hash directly cus it contains negative number
            create a hash, every idx(corresponding to the value in ofirin)
            conut from 0
            then sum from idx 0, when sum>=k, return the idx
        but we can have 2 hashes, one for positive, one for negative. 
        and count the negative one reversely
        O(n) (n+n)
        space: O(1)(very large)
        '''
        positive = [0]*(10**4+1)
        negative = [0]*(10**4+1)
        n = len(nums)
        for i in range(0, n):
            cur_num = nums[i]
            if cur_num >= 0:
                positive[cur_num] += 1
            else:
                negative[cur_num] += 1
        count = 0
        for i in range(len(positive)-1, -1, -1):
            count += positive[i]
            if count >= k:
                return i
        for i in range(-1, -len(negative)-1, -1):
            count += negative[i]
            if count >= k:
                return i

    def findKthLargestI(self, nums: List[int], k: int) -> int:
        '''
        heap solution: (manually implemented heap is slow)
        a smarter O(n)
        it's like 2 stack track biggest/smallest number
        keep updating the top of heap
        '''
        heap = []  # a min heap

        def heap_down(heap):
            if not heap:  # after pop the only elem in the heap, there'll be no elem to swap
                return
            heap[0], heap[-1] = heap[-1], heap[0]  # prepare to pop
            n = len(heap)
            idx = 0
            while idx < n-1:
                l_idx = idx*2+1
                r_idx = min(n-1, idx*2+2)
                if l_idx >= n:
                    return idx
                smaller_idx = l_idx if heap[l_idx] < heap[r_idx] else r_idx
                if heap[idx] <= heap[smaller_idx]:  # already
                    return idx
                heap[idx], heap[smaller_idx] = heap[smaller_idx], heap[idx]  # swap
                idx = smaller_idx
            return idx

        def heap_up(heap):  # O(logn)
            idx = len(heap)-1  # the new added elem
            while idx > 0:  # only need nums[i]<nums[parent_idx], since (0-1)/2==0
                parent_idx = (idx-1)//2
                if heap[parent_idx] <= heap[idx]:
                    return idx
                heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
                idx = parent_idx
            return idx

        for i in range(k):
            heap.append(nums[i])
            heap_up(heap)

        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heap[0], heap[-1] = heap[-1], heap[0]  # swap prepare to pop minimum
                heap.pop()
                heap_down(heap)
                heap.append(nums[i])
                heap_up(heap)
        return heap[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        time: O(n)
            partition size: m:logn (n, n/2, n/4...)
            every time partition: O(m)
        space: O(1) (im place)
        random choose solution
        similar with hash, that leverages idx
        instead of fully partition, only search in the more likely area
        (same as binary search)
        find kth large: find len(nums)-k idx num in ascending order sorted arr
        '''

        def partition(nums, start, end, pivot_idx):
            '''left: larger'''
            nums[start], nums[pivot_idx] = nums[pivot_idx], nums[start]  # swap
            pivot_num = nums[start]
            l, r = start, end
            idx = start
            while idx <= r:
                if nums[idx] > pivot_num:
                    nums[l], nums[idx] = nums[idx], nums[l]
                    l += 1
                    idx += 1
                elif nums[idx] == pivot_num:
                    idx += 1
                else:
                    nums[r], nums[idx] = nums[idx], nums[r]
                    r -= 1
            return l, idx-1

        def search(nums, start, end, k):
            if start >= end:
                return nums[start]
            pivot_idx = random.randint(start, end)
            mid_l, mid_r = partition(nums, start, end, pivot_idx)
            if mid_l <= k-1 <= mid_r:
                return nums[k-1]
            elif mid_r < k-1:  # current too large
                return search(nums, mid_r+1, end, k)
            else:  # current too small
                return search(nums, start, mid_l-1, k)

        def search_while(nums, k):
            start, end = 0, len(nums)-1
            while start < end:
                pivot_idx = random.randint(start, end)
                mid_l, mid_r = partition(nums, start, end, pivot_idx)
                if mid_l <= k-1 <= mid_r:
                    return nums[k-1]
                elif mid_r < k-1:  # current too large
                    start = mid_r+1
                else:
                    end = mid_l-1
            return start

        return search_while(nums, k)
        # return search(nums, 0, len(nums)-1, k)


t = [0]
# t = [0, 1]
# t = [-1]
# t = [1]
t = [1, 2, -1, -10]
t = [3, 2, 1, 5, 6, 4]
r = Solution().findKthLargest(t, 2)
print(r)
