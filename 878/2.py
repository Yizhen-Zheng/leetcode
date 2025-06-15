import math


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        '''
        O(log n), 
        converts 'find the target number' to 'find how many magic number', 
        if BS finds a point that makes 'the number of magic numbers' exactly the n, 
        we can say that least limit (form the nth number) is our target
        '''
        def gcd(a, b):
            while b != 0:
                r = a % b
                a = b
                b = r
            return a

        def lcm(a, b):
            return int(a / gcd(a, b)*b)

        MOD = 1000000007
        A = min(a, b)
        B = max(a, b)
        common_multiple = lcm(B, A)
        l = A
        r = n*A
        while l < r:
            m = int((l+r)/2)
            nums_can_be_divide = math.floor(m/A)+math.floor(m/B)-math.floor(m/common_multiple)
            if nums_can_be_divide >= n:
                r = m
            else:
                l = m+1
        return l % MOD


# t = (1, 2, 3)
# t = (4, 2, 3)
# t = (5, 2, 4)
t = (3, 6, 4)

r = Solution().nthMagicalNumber(t[0], t[1], t[2])
print(r)
