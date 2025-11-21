class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        bottom up 
        t: O(n)
        s: O(1)

        '''
        a, b = 1, 2
        if n <= 2:
            return n
        for _ in range(2, n):
            a, b = b, a+b
        return b


r = Solution().climbStairs(5)
print(r)
