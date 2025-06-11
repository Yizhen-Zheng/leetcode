import math


class Solution:
    def isUgly(self, n: int) -> bool:
        '''
        divide by target answer
        like purify or filter down the number
        '''

        ugly = [2, 3, 5]

        for d in ugly:
            while n % d == 0 and n > 0:
                n /= d

        return n == 1


# t = 1
# t = 6
t = 13
# t = 14
# t = 5
r = Solution().isUgly(t)
print(r)
