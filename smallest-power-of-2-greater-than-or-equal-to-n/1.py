class Solution:
    def solve(self, n: int) -> bool:
        '''
        O(1)(since time <=32, or a very small logn)
        n: > 0
        if only has 1 digit: return itself(like 0010 0000)
        0110 -> 1000
        find most significant digit
        '''
        if n < 1:
            return 1
        if n & (-n) == n:  # n itself is 2's power
            return n
        digit_count = 0
        m = n
        while m:
            m >>= 1
            digit_count += 1

        return 1 << digit_count

    def solve(self, n: int) -> bool:
        '''
        O(1)
        manually add to the next 2's power
        int is within 32 digit, 
         so we can manually flip all 0s to 1s after the most significant digit
        '''
        if n < 1:
            return 1
        n -= 1  # handle n itself is 2's power
        n |= n >> 1
        n |= n >> 2
        n |= n >> 4
        n |= n >> 8
        n |= n >> 16
        n |= n >> 32
        return n+1


t = -1
t = 1
t = 4
t = 129
# t = 9
r = Solution().solve(t)
print(r)
