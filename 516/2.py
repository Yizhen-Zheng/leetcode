class Solution:
    def longestPalindromeSubseqLcsI(self, s: str) -> int:
        '''
        try dp top down
        question: find all combination needs 2^n
        dp: 
        way1: find longest common subsequence of s and reversed_s

        '''
        rs = ''.join(reversed(list(s)))
        dp = [[0]*(len(s))for _ in range(len(s))]

        def rec(i, j):
            '''
            the same way as lcs
            '''
            if i < 0 or j < 0:
                return 0
            if dp[i][j] > 0:
                return dp[i][j]
            if s[i] == rs[j]:
                dp[i][j] = rec(i-1, j-1)+1
            else:
                a = rec(i-1, j)
                b = rec(i, j-1)
                dp[i][j] = max(a, b)
            return dp[i][j]

        r = rec(len(s)-1, len(s)-1)
        print(dp)
        return r

    def longestPalindromeSubseqLcsII(self, s: str) -> int:
        '''
        try dp top down
        question: find all combination needs 2^n
        dp: 
        way1: find longest common subsequence of s and reversed_s
        way2: dp: left and right
        '''
        rs = ''.join(reversed(list(s)))
        dp = [[0]*(len(s)+1)for _ in range(len(s)+1)]

        '''
        the same way as lcs
        when using for loop, we want the edge case handler(extra 0 columns,rows)
        why this can be monotonic: we know the more char we contain, the longer potential subs would be. 
        so just get max(a,b)
        'pdor'
        'ergpd'
        if we find both p, then there's no need to check 'p' vs 'erg' or '' vs 'ergp'
        '''
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == rs[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    a = dp[i-1][j]
                    b = dp[i][j-1]
                    dp[i][j] = max(a, b)

        print(dp)
        return dp[i][j]


t = ''
t = 'a'
t = 'cdd'
t = 'dded'
t = 'ahgfghz'
# r = Solution().longestPalindromeSubseqLcsI(t)
r = Solution().longestPalindromeSubseqLcsII(t)
print(r)
