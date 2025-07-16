from typing import List
import time


class Solution:

    def removeInvalidParenthesesRecII(self, s: str) -> List[str]:
        '''
        non-optimal, but in evolutino version
        first calculate how many need to remove
        by purning duplicated ones, this works fast
        '''
        rmL, rmR = 0, 0
        for char in s:
            if char == '(':
                rmL += 1
            elif char == ')':
                if rmL:
                    rmL -= 1
                else:
                    rmR += 1

        def dfs(i: int, rmL: int, rmR: int, pl: int, one: list[str], res: set[str]):
            '''     
            DFS to generate all valid strings
            i: current position in string s
            rmL: remaining left parentheses to remove
            rmR: remaining right parentheses to remove
            pl: current balance(open parentheses count)(if '('more than ')', pr>0, vice versa)
            one: current string being built
            res: result set
            since this is using an 'one' array for str building, we cannot use set to lookup every step since that requires join str(O(n)) each lookup
            so this need to use skip duplication
            '''
            # base case
            if i == len(s) or rmL < 0 or rmR < 0 or pl < 0:
                if rmL == 0 and rmR == 0 and pl == 0:
                    res.add(''.join(one))
                return
            char = s[i]
            if char == '(':
                if (not len(one)) or one[-1] != '(':
                    dfs(i+1, rmL-1, rmR, pl, one, res)
                one.append('(')
                dfs(i+1, rmL, rmR, pl+1, one, res)
            elif char == ')':
                if (not len(one)) or one[-1] != ')':
                    dfs(i+1, rmL, rmR-1, pl, one, res)
                one.append(')')
                dfs(i+1, rmL, rmR, pl-1, one, res)
            else:
                one.append(char)
                dfs(i+1, rmL, rmR, pl, one, res)
            if len(one) > 0:
                one.pop()
        res = set()
        one = []

        dfs(0, rmL, rmR, 0, one, res)
        return list(res)

    def removeInvalidParentheses(self, s: str) -> List[str]:
        '''
        num of parentheses may smaller than n, since s contains lower alphabets
        lack of early pruning to prevent duplicated cases (need a seen or skip '((((' in a row)
        increase lower boundary as we find smaller removal
        which is slow since we are depth first traverse and exploring potentially invalid branches
        '''
        parentheses = list(s)
        lower_boundary = 0
        res = set()

        def check(p) -> bool:
            count = 0
            for elem in p:
                if elem == '(':
                    count += 1
                elif elem == ')':
                    if count <= 0:
                        return False
                    count -= 1
            return count == 0

        def rec(p, boundary):
            if len(p) < boundary:
                return boundary
            if check(p):  # better than lower boundary
                new_boundary = len(p)
                p_str = ''.join(p)
                res.add(p_str)  # prevent duplicated
                return new_boundary

            new_boundary = boundary
            for i in range(len(p)):
                if not (ord('a') <= ord(p[i]) <= ord('z')):
                    newp = p[:i]+p[i+1:]
                    new_boundary = max(new_boundary, rec(newp, new_boundary))
            return new_boundary
        lower_boundary = rec(parentheses, lower_boundary)

        return list(filter(lambda x: len(x) == lower_boundary, list(res), ))

    def removeInvalidParentheses(self, s: str) -> List[str]:
        '''
        stack version DFS
        '''

        parentheses = list(s)
        lower_boundary = 0
        res = set()

        def check(p) -> bool:
            count = 0
            for elem in p:
                if elem == '(':
                    count += 1
                elif elem == ')':
                    if count <= 0:
                        return False
                    count -= 1
            return count == 0

        q = [parentheses]
        idx = 0
        while idx < len(q):
            cur = q[idx]
            idx += 1
            if len(cur) < lower_boundary:
                continue
            if check(cur):
                lower_boundary = max(lower_boundary, len(cur))
                cur_str = ''.join(cur)
                res.add(cur_str)  # prevent duplicated, exit this branch
            for i in range(len(cur)):
                if not (ord('a') <= ord(cur[i]) <= ord('z')):
                    newp = cur[:i]+cur[i+1:]
                    q.append(newp)

        return list(res)


t = ''
t = ')'
# t = '()'
# t = '())'
t = '()a)'
# t = '(())a))'
r = Solution().removeInvalidParenthesesRecII(t)
# r = Solution().removeInvalidParentheses(t)
print(r)
