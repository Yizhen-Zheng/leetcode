import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        '''
        9:10-9:48 38min
        search in 2 parts, seems multiple binary search
        all nums unique, so if arr[0]==arr[-1], arr is only one num
        BF: O(n),loop all
        origin sorted: ascending
        idea: find the rotate point, search in the corresponding part
        find where nums[p]>nums[p+1]
        detect where p lands on(left or right part: arr[0], arr[-1])
        '''
        n = len(nums)

        def search(lo: int, hi: int, target: int):
            l, r = lo, hi+1
            while l < r:
                m = l+(r-l)//2
                cur = nums[m]
                if cur > target:
                    r = m
                elif cur < target:
                    l = m+1
                else:
                    return m
            return -1
        if not nums[0] > nums[-1]:  # is not rotated
            i = search(0, n-1, target)
            return i
        # is rotated, find k
        le, ri = 0, n
        piv = nums[0]
        while le < ri:
            mid = le+(ri-le)//2
            if nums[mid] < piv:
                ri = mid
            else:
                le = mid+1
        if target < piv:
            return search(le, n-1, target)
        else:
            return search(0, le-1, target)

    def search(self, nums: list[int], target: int) -> int:
        '''
        solution
        the 2 cross left and right:
        if mid on left part, target on right part:
            move lo to mid+1(try to go right, the smaller part)
        if mid on right part, target on left part:
            move lo to mid(try to go left, the larger part)
        the 2 both mid and target either on left or right:
        search as normal, because we can only narrow down the range

        '''
        n = len(nums)
        lo, hi = 0, n
        piv = nums[0]
        while lo < hi:
            mid = lo+(hi-lo)//2
            if target < piv < nums[mid]:
                # H H H H L L
                # P     M T
                # move left to squeeze toward right
                lo = mid+1
            elif target >= piv > nums[mid]:
                # H H H L L L
                # P T   M
                # move right to squeeze toward left
                hi = mid
            elif nums[mid] < target:
                # H H H H H T T T T
                # P   M T

                # H H H H H T T T T
                # P           M T

                # move left to squeeze toward right
                lo = mid+1
            elif nums[mid] > target:
                # H H H H H T T T T
                # P   T M

                # H H H H H T T T T
                # P         T M

                # move right to squeeze toward left
                hi = mid
            else:
                return mid
        return -1


t = [4, 5, 6, 0, 1, 2]
r = Solution().search(t, -1)
print(r)
