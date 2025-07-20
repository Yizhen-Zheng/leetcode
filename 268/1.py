class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        '''
        a notmal hash, or use XOR
        '''
        actual_sum = 0
        expected_sum = 0
        for n in nums:
            actual_sum ^= n
        for i in range(0, len(nums)+1):
            expected_sum ^= i
        return expected_sum ^ actual_sum


t = [0, 2]
t = [1, 2]
t = [1, 3, 0]
t = [3, 0, 1]
r = Solution().missingNumber(t)
print(r)
