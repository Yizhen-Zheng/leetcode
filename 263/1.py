import math


class Solution:
    def isUgly(self, n: int) -> bool:
        '''
        find from 2 to square root (the rest of num are same as the prev we've checked)
        (2 * 13, if we've checked 2, we don't need to check 13)
        slow answer
        O(n**2)
        '''
        def is_prime(num):
            for i in range(2, math.ceil(math.sqrt(num))+1):
                if num % i == 0:
                    return False
            return True

        ugly = [2, 3, 5]

        for i in range(2, n+1):
            if n % i == 0:
                j = n/i
                if is_prime(i):
                    if i not in ugly:
                        return False
                if is_prime(j):
                    if j not in ugly:
                        return False

        return True


# t = 6
t = 13
# t = 14
# t = 5
r = Solution().isUgly(t)
print(r)
