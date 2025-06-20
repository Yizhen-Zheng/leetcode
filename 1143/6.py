

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        try to memorization (top-down)
        TODO: debug
        '''
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        m = len(text1)+1
        n = len(text2)+1
        dp = [0]*(n)
        print(text1, text2)
        # first dummy value to reduce handle j=0, j-1=-1
        for i in range(1, m):
            prev_r_prev_c = 0
            for j in range(1, n):
                prev_r_curr_c = dp[j]
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
                    dp[j] = 1+prev_r_prev_c
                else:
                    dp[j] = max(dp[j-1], prev_r_curr_c)
                prev_r_prev_c = prev_r_curr_c
            print(dp, text1[i-1])

        return dp[-1]


# t = ('', '')
t = ('fz', 'afc')
# t = ('afe', 'fz')
t = ('erb', 'rbde')
# t = ('errb', 'rbde')
t = ("bsbininm", 'jmjkbkjkv')
# t = ('afcdae', 'azf')
# t = ('aezzzzzz', 'azfzfz')
# t = ('aez', 'aze')
r = Solution().longestCommonSubsequence(t[0], t[1])
print(r)
