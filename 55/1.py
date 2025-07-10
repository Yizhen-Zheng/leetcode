from typing import List


class Solution:
    def canJumpI(self, nums: List[int]) -> bool:
        '''
        '''

        current_max = 0
        for i in range(len(nums)-1):
            current_max = max(current_max, nums[i])
            if current_max == 0:
                return False
            current_max -= 1
        return True

    def canJump(self, nums: List[int]) -> bool:
        '''
        '''
        current_max = 0
        for n in nums:
            if current_max < 0:
                return False
            current_max = max(current_max, n)
            current_max -= 1
        return True


t = [0, 1, 2, 3]
# t = [1, 0]
# t = [0]
t = [1, 0, 0]
r = Solution().canJump(t)
print(r)
