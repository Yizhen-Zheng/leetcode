class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''
        first get all different bits
        then same as count ones
        '''
        diff = x ^ y
        res = 0
        while diff:
            res += (diff & 1)
            diff >>= 1
        return res

    def hammingDistance(self, x: int, y: int) -> int:
        '''
        reduce from 1 -> 2
        reduce from 2 -> 4
        reduce from 4 -> 8
        reduce from 8 -> 16
        reduce from 16 -> 32
        '''
        diff = x ^ y
        diff = (diff & 0x55555555)+((diff & 0xAAAAAAAA) >> 1)
        diff = (diff & 0x33333333)+((diff & 0xCCCCCCCC) >> 2)
        diff = (diff & 0x0F0F0F0F)+((diff & 0xF0F0F0F0) >> 4)
        diff = (diff & 0x00FF00FF)+((diff & 0xFF00FF00) >> 8)
        diff = (diff & 0x0000FFFF)+((diff & 0xFFFF0000) >> 16)
        return diff


t = [1, 9]
t = [3, 5]
r = Solution().hammingDistance(t[0], t[1])
print(r)
