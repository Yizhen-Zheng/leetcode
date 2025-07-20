class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        verify if it only has 1 digit that is 1
        '''
        if n < 1:  # NOTE 1 is 2's power!
            return False
        count_shift = 0
        m = n
        while n:
            if n & 1:
                break
            n >>= 1
            count_shift += 1
        print(n)
        print(1 << count_shift)
        return m == (1 << count_shift)

    def isPowerOfTwo(self, n: int) -> bool:
        '''
        least significan digit
        print(-4&(4))
        4
        this also handle negaive
        '''
        return n == (n & (-n)) if n > 0 else False


t = 3
t = 1024
r = Solution().isPowerOfTwo(t)
print(r)
