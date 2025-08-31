class Solution:
    def search(self, nums: list[int], target: int) -> int:
        '''
        10:35-1-:38
        '''
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo+(hi-lo)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid+1
            else:
                hi = mid
        return -1
