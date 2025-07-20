class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        '''
        use XOR, space: O(1)
        '''
        res = 0
        for n in nums:
            res ^= n
        return res
