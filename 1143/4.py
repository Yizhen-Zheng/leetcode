

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        try to memorization (Top down)
        this collect the result eventually at 1st grid
        '''
        m = len(text1)
        n = len(text2)
        dp = [[0]*n for _ in range(m)]

        def rec_forward(i, j):
            '''this collect the result eventually at 1st grid'''
            if i > m-1 or j > n-1:
                return 0
            if dp[i][j]:
                return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] = 1 + rec_forward(i+1, j+1)

            else:
                a = rec_forward(i, j+1)
                b = rec_forward(i+1, j)

                dp[i][j] = max(a, b)

            return dp[i][j]

        def rec_back(i, j):
            '''this collect the result eventually at last grid'''

            if i < 0 or j < 0:
                return 0
            if dp[i][j]:
                return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] = 1 + rec_back(i-1, j-1)

            else:
                a = rec_back(i, j-1)
                b = rec_back(i-1, j)

                dp[i][j] = max(a, b)

            return dp[i][j]

        # res = rec_forward(0, 0)
        res = rec_back(m-1, n-1)
        print(dp)
        return res


# t = ('', '')
# t = ('abcde', 'ace')
# t = ('afcde', 'oze')
# t = ('erb', 'rbde')
# t = ('errb', 'rbde')
t = ("bsbininm", 'jmjkbkjkv')
# t = ('afcdae', 'azf')
# t = ('aezzzzzz', 'azfzfz')
# t = ('aez', 'aze')
r = Solution().longestCommonSubsequence(t[0], t[1])
print(r)
