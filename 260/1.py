class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        '''

        '''
        xor_a_b = 0
        for n in nums:
            xor_a_b ^= n
        a, b = 0, 0
        LSB_difference = xor_a_b & (-xor_a_b)
        for n in nums:
            if (n & LSB_difference) != 0:  # have same bit
                a ^= n
            else:
                b ^= n
        return [a, b]

    def singleNumber(self, nums: list[int]) -> list[int]:
        '''

        '''
        xor_a_b = 0
        for n in nums:
            xor_a_b ^= n
        a = 0
        LSB_difference = xor_a_b & (-xor_a_b)
        for n in nums:
            if (n & LSB_difference) != 0:  # have same bit
                a ^= n

        return [a, xor_a_b ^ a]


t = [1, 1, 2, 3]
# t = [1, 1, 7, 3, 12, 12]
r = Solution().singleNumber(t)
print(r)
