class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        a-smart-solution use db to trsck numbers as well
        '''
        dp = [0] * len(s)
        idx = 0
        maximum = 0
        while idx < len(s):
            cur = s[idx]
            if idx > 0 and cur == ')':
                prev_idx = idx-dp[idx-1]-1
                if prev_idx >= 0 and s[prev_idx] == '(':
                    dp[idx] = dp[idx-1]+2
                    if prev_idx > 1:
                        dp[idx] += dp[prev_idx-1]

            maximum = max(dp[idx], maximum)
            idx += 1
        print(dp)

        return maximum


# t = '('
# t = ')'
# t = ''
t = '()'
# t = '))())'
# t = '((()))'
# t = '()((()'
# t = ")()())()()("
r = Solution().longestValidParentheses(t)
print(r)
