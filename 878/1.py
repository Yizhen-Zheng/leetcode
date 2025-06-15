class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        '''
        O(n), TLE
        '''
        def gcd(a, b):
            while b != 0:
                r = a % b
                a = b
                b = r
            return a

        def lcm(a, b):
            return a % gcd(a, b)*b

        MOD = 1000000007
        m = []
        A = 1
        B = 1
        res = 0
        for _ in range(n):
            ma = A*a
            mb = B*b
            next_m = min(ma, mb)
            if next_m == ma:
                A += 1
            if next_m == mb:
                B += 1
            res = next_m % MOD
            print(res)
        return res


t = (1, 2, 3)
# t = (4, 2, 3)
# t = (1, 2, 3)
r = Solution().nthMagicalNumber(t[0], t[1], t[2])
print(r)
