class Solution:
    def longestPalindromeSubseqLcsI(self, s: str) -> int:
        '''
        try dp top down
        question: find all combination needs 2^n
        dp
        way2: dp: left and right
        try top down
        '''
        dp = [[0]*(len(s))for _ in range(len(s))]

        def rec(l, r):
            '''
            '''
            if l > r or l < 0 or r < 0 or l >= len(s) or r >= len(s):
                return 0
            if dp[l][r]:
                return dp[l][r]
            if l == r:
                dp[l][r] = 1
            elif s[l] == s[r]:
                dp[l][r] = rec(l+1, r-1)+2
            else:
                a = rec(l+1, r)
                b = rec(l, r-1)
                dp[l][r] = max(a, b)
            return dp[l][r]

        r = rec(0, len(s)-1)
        print(dp)
        return r


t = ''
t = 'a'
# t = 'cdd'
# t = 'dded'
t = 'ahgfghz'
r = Solution().longestPalindromeSubseqLcsI(t)

print(r)
