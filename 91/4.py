

class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        improved version: handle edge case
        '''
        dp = [-1]*(len(s)+1)
        dp[-1] = 1

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue
            else:
                dp[i] = dp[i+1]
            if i+1 < len(s) and (int(s[i] + s[i+1]) < 26):
                dp[i] += dp[i+2]
        return dp[0]


# t = '1'
# t = '1203'
# t = '226'
# t = '60'
t = '06'
# t = '10'
# t = '12'
# t = '1212121'
r = Solution().numDecodings(t)
print(r)
