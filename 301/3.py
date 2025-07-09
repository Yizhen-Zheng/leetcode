from typing import List
import time


class Solution:

    def removeInvalidParentheses(self, s: str) -> List[str]:
        '''
        how to use reversed in a str:
            >> my_str='hello'
            >> r=reversed(my_str)
            >> print(r)
            <reversed object at 0x1053b73a0>
            >> print(''.join(r))
            olleh
            >>> 
        '''
        ans = []

        def remove_helper(s, ans, prev_i, prev_j, open, close):
            counter = 0
            for i in range(prev_i, len(s)):
                if s[i] == open:
                    counter += 1
                if s[i] == close:
                    counter -= 1
                if counter < 0:
                    for j in range(prev_j, i+1):
                        if s[j] == close and (j == 0 or s[j-1] != close):
                            new_s = s[:j]+s[j+1:]
                            remove_helper(new_s, ans, i, j, open, close)
                    return
            # at the time point we first reach here, we know right parentheses are cleaned
            s = s[::-1]
            if open == ')':
                # if we get here again, we need to exit
                ans.append(s)
                return
            remove_helper(s, ans, 0, 0, ')', '(')

        remove_helper(s, ans, 0, 0, '(', ')')
        return ans

    def removeInvalidParenthesesI(self, s: str) -> List[str]:
        '''

        '''

        p = list(s)
        ans = []

        def remove(s, ans, last_i, last_j, l, r):
            counter = 0
            for i in range(last_i,  len(s)):
                if s[i] == l:
                    counter += 1
                elif s[i] == r:
                    counter -= 1
                if counter < 0:
                    # once find new extra right par, remove immediately
                    for j in range(last_j, i+1):
                        if s[j] == r and (j == last_j or s[j-1] != r):
                            # always remove first encountered ')' and skip duplicated
                            # (like s[2] and s[3] are same in'()))')
                            remove(s[:j]+s[j+1:], ans, i, j, l, r)
                    return
            # if no invalid ')', we'll get here
            reversed_s = list(reversed(s))
            if l == '(':
                remove(reversed_s, ans, 0, 0, ')', '(')
            else:
                # get here means we're done to clean up reversed as well, and reversed it back
                ans.append(''.join(reversed_s))
        remove(p, ans, 0, 0, '(', ')')
        return ans


t = ''
t = '()'
t = '())'
t = '()a)'
t = '(())a))'
t = "()())()"
t = "()())()))e))))"
t = "()(((((((((((((e)"
start = time.time()
r = Solution().removeInvalidParentheses(t)
end = time.time()
print(end-start)
print(r)
