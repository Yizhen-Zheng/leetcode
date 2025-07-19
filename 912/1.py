from typing import List
import time

# TODO:Tim sort,
# TODO:shell sort,
# TODO:cyclic sort

'''
stability: need at least O(N) space complexity so far
(merge, count, radix, bubble, insert)
'''


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''
        try while version
        assign slicing:
        >> l1=[1,2,3,4,5,6]
        >> l1[:3]=[0,0,0,]
        >> print(l1)
        >> [0, 0, 0, 4, 5, 6]

        return nums! not merged. since if we have single elem like[30], with unit_len<n, merged won't be called

        why unit_len<n: it's proved r = l+2*unit_len, so we don't need duplicated check, which will cause an extra loop.
        but the extra loop seems only happen once and exit immediately(since unit length is n, and merge will exit immediately as well)

        |___________|___________|
        l           m(n)        r

        why merge sort is faster:
        every comparison is reserved and formed valid order

        '''
        def merge(a, b):
            ptr_a = ptr_b = 0
            merged = []
            while ptr_a < len(a) and ptr_b < len(b):
                if a[ptr_a] <= b[ptr_b]:  # left <= right: stability
                    merged.append(a[ptr_a])
                    ptr_a += 1
                else:
                    merged.append(b[ptr_b])
                    ptr_b += 1
            if ptr_a < len(a):
                merged.extend(a[ptr_a:])
            if ptr_b < len(b):
                merged.extend(b[ptr_b:])
            return merged
        n = len(nums)
        unit_len = 1
        while unit_len < n:
            l = r = 0
            for i in range(0, n, unit_len << 1):
                # process 2 unit len per iterate,
                # so if unit len is 1, improve 2;
                # if unit len is 2, improve 4...
                l = i
                m = l+unit_len
                r = m+unit_len
                a = nums[l:m]
                b = nums[m:r]
                # if m < n: #prevent extra check?
                # seems it won't cause serious issue without the check,
                # but with other language, we definitly need to check m and r
                merged = merge(a, b)
                nums[l:r] = merged
            unit_len *= 2

        return nums


t = [100]
t = [3, 5, 7, 0, 8, -2, 89, 46, 0,]
# t = [3, 5, 7, 0, 8, 56, 89, 46, 32, 578, 2, 4, 921, 89, 0, -2,
#  4, 34, 13, 97, 96, 46, 99, 33, 546, 72, -5, -8, 301, -304]
s = time.time()
r = Solution().sortArray(t)
e = time.time()
print(r)
print(e-s)
