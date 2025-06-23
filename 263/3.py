import math


class Solution:
    def isUgly(self, n: int) -> bool:
        '''
        review
        prime number except 2,3,5 is all not ugly(have prime factor themselves)
        check if they can be devided by 2,3,5 until 1
        '''
        if n > 0:
            while n:
                if n == 1:
                    return True
                a = n % 2
                b = n % 3
                c = n % 5
                if a == 0 or b == 0 or c == 0:
                    if a == 0:
                        n /= 2
                    if b == 0:
                        n /= 3
                    if c == 0:
                        n /= 5
                    # n = int(n)
                    continue
                break
        return False


# t = 1
t = 6
# t = 13
# t = 14
# t = 5
r = Solution().isUgly(t)
print(r)
