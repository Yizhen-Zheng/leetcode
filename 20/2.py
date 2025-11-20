class Solution:
    def isValid(self, s: str) -> bool:
        '''
        19:24-19:36
        '''
        if len(s) % 2:
            return False
        stk = []
        for p in s:
            if p == '(' or p == '[' or p == '{':
                stk.append(p)
            else:
                if stk and (
                        (p == ')' and stk[-1] == '(') or
                        (p == ']' and stk[-1] == '[') or
                        (p == '}' and stk[-1] == '{')):
                    stk.pop()
                else:
                    return False
        return len(stk) == 0


t = ']'
r = Solution().isValid(t)
print(r)
