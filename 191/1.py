class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        '''
        count = 0
        while n:
            count += (n & 1)
            n >>= 1
        return count

    def hammingWeight(self, n: int) -> int:
        '''
        divide and conquer
        first compression: 
        number of ones on each digit(either 0 or 1) -> number of ones on each 2 digit (0 / 1 / 11)
        number of ones on each 2 digit -> number of ones on each 4 digit (0000 ~ 0100)
        number of ones on each 4 digit -> number of ones on each 8 digit (0000 ~ 1000)
        number of ones on each 8 digit -> number of ones on each 16 digit (0000 0000 ~ 0001 0000)
        number of ones on each 16 digit -> number of ones on each 32 digit (0000 0000 ~ 0010 0000)
        '''
        n = (n & 0x55555555)+((n >> 1) & 0x55555555)
        n = (n & 0x33333333)+((n >> 2) & 0x33333333)
        n = (n & 0x0F0F0F0F)+((n >> 4) & 0x0F0F0F0F)
        n = (n & 0x00FF00FF)+((n >> 8) & 0x00FF00FF)
        n = (n & 0x0000FFFF)+((n >> 16) & 0x0000FFFF)
        return n


t = 0
# t = 1
t = 255
# t = 1024
r = Solution().hammingWeight(t)
print(r)
