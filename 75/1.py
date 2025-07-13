from typing import List
import random


class Solution:
    def sortColorsI(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def partition(nums, low, high, pivot_idx):
            nums[low], nums[pivot_idx] = nums[pivot_idx], nums[low]
            pivot_num = nums[low]
            l, r = low, high
            ptr = low
            while ptr <= r:
                if nums[ptr] == pivot_num:
                    ptr += 1
                elif nums[ptr] < pivot_num:
                    nums[l], nums[ptr] = nums[ptr], nums[l]
                    l += 1
                    ptr += 1
                elif nums[ptr] > pivot_num:
                    nums[r], nums[ptr] = nums[ptr], nums[r]
                    r -= 1
            return l-1, ptr

        n = len(nums)
        if n < 2:
            return
        for i in range(0, n):
            if nums[i] == 1:
                partition(nums, 0, n-1, i)
                return
        partition(nums, 0, n-1, 0)

    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums)-1
        ptr = 0
        while ptr <= r:
            if nums[ptr] == 0:
                nums[l], nums[ptr] = nums[ptr], nums[l]
                ptr += 1
                l += 1
            elif nums[ptr] == 1:
                ptr += 1
            else:
                nums[r], nums[ptr] = nums[ptr], nums[r]
                r -= 1


t = [0]
t = [0, 0]
t = [2]
# t = [2, 2]
# t = [1]
# t = [1, 1]
# t = [1, 0, 2]

r = Solution().sortColors(t)
print(t)
