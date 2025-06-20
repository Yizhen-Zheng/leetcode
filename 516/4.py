class Solution:
    def longestPalindromeSubseqLcsI(self, s: str) -> int:
        '''
        try dp top down
        question: find all combination needs 2^n
        dp
        way2: dp: left and right
        try buttom up
        '''
        if not len(s):
            return 0
        dp = [[0]*(len(s))for _ in range(len(s))]

        for l in range(len(s)-1, -1, -1):
            for r in range(l, len(s)):
                if l == r:
                    dp[l][r] = 1
                elif s[l] == s[r]:
                    dp[l][r] = dp[l+1][r-1]+2
                else:
                    dp[l][r] = max(dp[l+1][r], dp[l][r-1])

        print(dp)
        return dp[0][-1]

    def longestPalindromeSubseqLcsII(self, s: str) -> int:
        '''
        try dp top down
        question: find all combination needs 2^n
        dp
        way2: dp: left and right
        try buttom up
        compress space: 2 row dp
        '''
        if not len(s):
            return 0
        dp = [[0]*(len(s))for _ in range(2)]

        for l in range(len(s)-1, -1, -1):
            for r in range(l, len(s)):
                if l == r:
                    dp[l % 2][r] = 1
                elif s[l] == s[r]:
                    dp[l % 2][r] = dp[(l+1) % 2][r-1]+2
                else:
                    dp[l % 2][r] = max(dp[(l+1) % 2][r], dp[l % 2][r-1])

        print(dp)
        return dp[0][-1]

    def longestPalindromeSubseqLcsIII(self, s: str) -> int:
        '''
        try dp top down
        question: find all combination needs 2^n
        dp
        way2: dp: left and right
        try buttom up
        compress space: 2 row dp
        '''
        if not len(s):
            return 0
        dp = [0]*len(s)

        for l in range(len(s)-1, -1, -1):
            prev_r_prev_c = 0
            for r in range(l, len(s)):
                prev_r_cur_c = dp[r]
                if l == r:
                    dp[r] = 1
                elif s[l] == s[r]:
                    dp[r] = prev_r_prev_c+2
                else:
                    dp[r] = max(dp[r], dp[r-1])
                prev_r_prev_c = prev_r_cur_c
        print(dp)
        return dp[-1]


t = ''
t = 'a'
# t = 'cdd'
t = 'dded'
t = 'ahgfgh'
# r = Solution().longestPalindromeSubseqLcsI(t)
# r = Solution().longestPalindromeSubseqLcsII(t)
r = Solution().longestPalindromeSubseqLcsIII(t)

print(r)
