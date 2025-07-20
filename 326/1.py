class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''
        '''
        if n < 1:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            n /= 3
        return True

    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1

    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (3**19 % n == 0)


t = -1
# t = 1
t = 4
t = 18
t = 9
r = Solution().isPowerOfThree(t)
print(r)
