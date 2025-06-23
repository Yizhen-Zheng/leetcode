import math


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        '''
        assume a<b
        '''
        a, b = min(a, b), max(a, b)
        MOD = 1000000007
        right = a*n
        left = a

        def greatest_common_divisor(a, b):
            # a>b>0
            a, b = max(a, b), min(a, b)
            while b != 0:
                a, b = b, a % b
            return a

        def least_common_multiple(a, b):
            gcd = greatest_common_divisor(a, b)
            return int(a / gcd * b)
        lcm = least_common_multiple(a, b)
        while left < right:
            # print(left, right)
            mid = int((right+left) / 2)
            num_of_magical_number = (int(mid/a)+int(mid/b)) - int(mid/lcm)
            if num_of_magical_number >= n:
                print(right)
                right = mid
            else:
                print(left)
                left = (mid+1)
        return left % MOD


t = (3, 2, 5)
t = (100, 2, 5)
t = (1000000000, 40000, 40000)
r = Solution().nthMagicalNumber(t[0], t[1], t[2])
print(r)
