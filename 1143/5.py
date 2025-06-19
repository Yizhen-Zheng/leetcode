

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        try to memorization (top-down)

        '''
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        m = len(text1)+1
        n = len(text2)+1
        dp = [[0]*n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if text1[i-1] == text2[j-1]:
                    '''
                    'ccre', 'era': 
                      c c r e
                    e
                    r
                    a
                    when find r==r: 
                    er, ccr
                    can only use e,cc
                    '''

                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        [print(r) for r in dp]
        return dp[-1][-1]


# t = ('', '')
t = ('fz', 'afc')
# t = ('afe', 'fz')
# t = ('erb', 'rbde')
# t = ('errb', 'rbde')
t = ("bsbininm", 'jmjkbkjkv')
# t = ('afcdae', 'azf')
# t = ('aezzzzzz', 'azfzfz')
# t = ('aez', 'aze')
r = Solution().longestCommonSubsequence(t[0], t[1])
print(r)
