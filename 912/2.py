import random
import time
from typing import List

'''
seems quick sort is very space efficient (buz merge needs to create temp new array)
Quicksort 
    O(log n) stack depth, each level swap in place
Mergesort 
    O(log n) stack depth  each level creates O(n) temporary space
    
why random choice:
if we have [1,2,3,4,5], and only choose last elem, 
then every recursion will need O(n), and need n iteration. so worst case will be O(n^2)
and space complexity is O(n*n)(n stack depth)
with random or middle pivot:
O(nlogn), buz we divide into 1/2 every time
and space complexity is O(logn). (depth of a binary tree)
'''
'''
lomuto_partion:
    first: if choose a non-last elem: move it to last first
    low: start idx
    high: end idx
    use the last elem in arr as partion idx 
     | 2,4,7,8,4,0,3|
    i  j
    i: the boundary of smaller than pivot area
    j: the boundary of traversed | not traversed yet
     smaller than pivot|greater than pivot| not traversed | pivot
    -1                 i                    j          
    note that j never reaches high, so we won't move pivot accidentally in a unpredictable way
    at the end, handle pivot 
    [2,1,4] -> i+1 == j at the end 
    [2,1,5,4] -> i+1 == 2, j==3 at the end
    no matter current nums[i] is greater  
    for j in range(n):
    # unlike while loop which j will eventually out of range, 
    # j will be at the last valid (n-1) after exiting the loop
'''
'''
optimized partition:
    handle when many numbers=pivot 
    eventually:
    [3,4,4,4,7,5]
        l.    idx
'''


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def optimized_partition(nums, low, high, pivot_idx):

            l, r = low, high
            idx = low
            nums[low], nums[pivot_idx] = nums[pivot_idx], nums[low]
            pivot = nums[low]
            while idx <= r:
                if nums[idx] > pivot:
                    nums[idx], nums[r] = nums[r], nums[idx]
                    r -= 1
                elif nums[idx] < pivot:
                    nums[idx], nums[l] = nums[l], nums[idx]
                    l += 1
                    idx += 1
                else:
                    idx += 1
            return l-1, idx

        def optimized_quicksort_rec(nums, start, end):
            if start >= end:
                return
            pivot_idx = random.randint(start, end)  # randint is inclusive!
            mid_l, mid_r = optimized_partition(nums, start, end, pivot_idx)
            # mid = hoare_partion(nums, start, end, pivot_idx)
            optimized_quicksort_rec(nums, start, mid_l)
            optimized_quicksort_rec(nums, mid_r, end)
            return nums

        def optimized_quicksort_stack(nums, start, end):
            '''different from merge sort, cannot use a for loop to simulate rec'''
            stack = [(0, len(nums)-1)]
            while stack:
                start, end = stack.pop()
                if start < end:
                    pivot_idx = random.randint(start, end)
                    mid_l, mid_r = optimized_partition(nums, start, end, pivot_idx)
                    stack.append((start, mid_l))
                    stack.append((mid_r, end))

            return nums

        def hoare_partion(nums, low, high, pivot_idx):
            '''
            put pivot to first 
            '''
            i, j = low, high
            nums[low], nums[pivot_idx] = nums[pivot_idx], nums[low]
            pivot = nums[low]
            while i <= j:
                if nums[i] > pivot and nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                if nums[i] <= pivot:
                    i += 1
                if nums[j] > pivot:
                    j -= 1
            nums[j], nums[low] = nums[low], nums[j]  # put 1st back
            return j

        def lomuto_partion(nums, low, high, pivot_idx):
            nums[pivot_idx], nums[high] = nums[high], nums[pivot_idx]
            pivot = nums[high]
            i = low-1
            for j in range(low, high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]  # change in place

            nums[i+1], nums[high] = nums[high], nums[i+1]  # swap pivot to boundary(left is smaller, right is bigger)
            return i+1  # where the pivot point

        def quicksort_rec(nums, start, end):
            if start >= end:
                return
            pivot_idx = random.randint(start, end)  # randint is inclusive!
            mid = lomuto_partion(nums, start, end, pivot_idx)
            # mid = hoare_partion(nums, start, end, pivot_idx)
            quicksort_rec(nums, start, mid-1)
            quicksort_rec(nums, mid+1, end)
            return nums

        optimized_quicksort_stack(nums, 0, len(nums)-1)
        # optimized_quicksort_rec(nums, 0, len(nums)-1)
        # quicksort_rec(nums, 0, len(nums)-1)
        return nums


t = [100]
t = [3, 5, 7, 0, 8, -2, 89, 46, 0,]
# t = [5, 2, 3, 1]
# t = [3, 5, 7, 0, 8, 56, 89, 46, 32, 578, 2, 4, 921, 89, 0, -2,
#  4, 34, 13, 97, 96, 46, 99, 33, 546, 72, -5, -8, 301, -304]
s = time.time()
r = Solution().sortArray(t)
e = time.time()
print(r)
print(e-s)
