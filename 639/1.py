class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        str of nums, may contain *, can be 1-9
        *-> 9 ; 3*->9; *2->9+2; 2*->15; **->9+9+6
        travel from tail to head
        *num: 9 + 2 or 1 *prev (prev > 6: 1, prev < 6: 2)
        num*: 1,2: +9 or +6
        if 1, 2 + *
        '''
        if s[0] == '0':
            return 0

        dp = [None]*(len(s)+1)
        dp[-1] = 1

        def check_ways(i):
            '''count extra ways (when 2 char can be paired)'''
            if s[i] == '*':
                # *0, *[1~6], *[7~9]
                if s[i+1] in '0123456':
                    # *0, *[1~6]
                    return dp[i+2]*2
                elif s[i+1] in '789':
                    # *[7~9]
                    return dp[i+2]
                else:
                    # *[*]
                    return dp[i+2]*15

            elif s[i] == '1':
                # 1[0~9], 1[*]
                if s[i+1] in '0123456789':
                    return dp[i+2]
                else:
                    # when 1[*]
                    return dp[i+2]*9

            elif s[i] == '2':
                # 2[0~6],2[*]
                if s[i+1] in '0123456':
                    return dp[i+2]
                elif s[i+1] == '*':
                    return dp[i+2]*6
            return 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue
            elif s[i] == '*':
                dp[i] = 9*dp[i+1]
            else:
                dp[i] = dp[i+1]
            if i < len(s)-1:
                dp[i] += check_ways(i)
            dp[i] = dp[i] % (1000000007)
        print(dp)
        return dp[0]


# t = '1*'
# t = '1*203'
t = '22*6'
# t = '*0'
# t = '10'
# t = '1212121'
# t = "*1*1*0"
r = Solution().numDecodings(t)
print(r)
