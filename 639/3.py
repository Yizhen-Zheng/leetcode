class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        ???not sure how to works yet
        https://leetcode.com/problems/decode-ways-ii/solutions/105274/python-straightforward-with-explanation
        e1: if prev is 1, how many ways we can form
        e1: if prev is 2, how many ways we can form
        e0: for single current char, how many ways we can form
        '''
        MOD = 1000000007
        e0, e1, e2 = 1, 0, 0
        for c in s:
            if c == '*':
                f0 = 9*e0+9*e1+6*e2
                f1 = e0
                f2 = e0
            else:
                f0 = (c > '0')*e0 + e1 + (c <= '6')*e2
                f1 = (c == '1')*e0
                f2 = (c == '2')*e0
                e0, e1, e2 = f0 % MOD, f1, f2

        return e0


# t = '1*'
# t = '1*203'
t = '22*6'
# t = '*0'
# t = '10'
# t = '1212121'
# t = "*1*1*0"
r = Solution().numDecodings(t)
print(r)
