'''
we need to store nums into 10 buckets
so how to do this without an arr of queues:
count how many size we need to allocate from 0-9 previously,   
and make then in one arr and accumulate the size in each idx
e,g, [10,33,23,7]
[0,0,0,0,0,0,0,0,0,0]  <- how many num each digit
 0,1,2,3,4,5,6,7,8,9
[1,1,1,3,3,3,3,4,4,4]  <- how many num so far
and use this idx to map back to origin arr
so we don't need 10 queues and loop from bucket for digit 0, popleft, append into new built arr

and, we need to count as we put numbers.
for example, for [4,44,5], bucket limit is 2, 1
first in: 4, count=1
second in: 44, count=2, we know we've finished all nums end with 4 

if we go through origin arr with forward iterate order we could maintain stable by:
get bucket idx -> store START idx in bucket_size arr
[0,0,0,0,0,2,3,3,3,3]  <- how many num each digit
 0,1,2,3,4,5,6,7,8,9
when puting back to new_arr, increase idx each time
[4,None,None]
[0,0,0,0,1,2,3,3,3,3]  <- add 4 to idx of 4, so 44 will find its idx as 1 

handle minus num: 
pick minimum num(like -10), for all elems, substract this number, 
so all elems are now positive
after sorting, add that minus number back
'''
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def count_sort(nums, offset_digit, base):
            n = len(nums)
            new_arr = [0]*n
            # count how many numbers on each bucket for that digit
            # e,g, [19, 29] will use 2 position in one bucket
            bucket_size = [0]*base
            for i in range(n):
                # e,g, 19: 9, 24: 4 for single digit
                idx = nums[i]//offset_digit % base
                bucket_size[idx] += 1
            for i in range(1, base):
                # change to: up to 5, there're n nums(so it accumulates from 0 to 9)
                bucket_size[i] += bucket_size[i-1]
            for i in range(n-1, -1, -1):
                num = nums[i]
                # get where to ask idx we should put elem into that response to it's origin order in arr
                bucket_idx = num//offset_digit % base
                new_arr_idx = bucket_size[bucket_idx]-1
                new_arr[new_arr_idx] = num
                bucket_size[bucket_idx] -= 1
            nums[::] = new_arr[::]
            return

        def radix_sort(nums, base):
            n = len(nums)
            min_elem = min(nums)
            if min_elem < 0:  # handle minus
                for i in range(n):
                    nums[i] -= min_elem
            max_elem = max(nums)
            offset_digit = 1
            while offset_digit <= max_elem:
                count_sort(nums, offset_digit, base)
                offset_digit *= base
            if min_elem < 0:
                for i in range(n):
                    nums[i] += min_elem

            return nums
        return radix_sort(nums, 100)  # adjust base param effects run time


t = [10, 9, 1]
t = [5, 2, 3, 1]
# t = [1, 0, 0, ]
# t = [9, 12, 2, 0]
# t = [-1, 2, -8, -10]
r = Solution().sortArray(t)
print(r)
