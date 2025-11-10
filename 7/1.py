class Solution:
    def reverse(self, x: int) -> int:
        '''
        19min
        overflow: in other language, INT_MAX+1=INT_MIN
        '''
        original = x
        x = abs(x)
        l, h = -(1 << 31), 1 << 31
        renum = 0
        while x != 0:
            last_digit = x % 10
            renum *= 10
            renum += last_digit
            x //= 10
        if renum > h or renum < l:
            return 0
        return renum if original >= 0 else -renum


t = 12
t = -12
r = Solution().reverse(t)
print(r)
