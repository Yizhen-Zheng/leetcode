from typing import List
import time


class Solution:

    def removeInvalidParentheses(self, s: str) -> List[str]:
        '''
        num of parentheses may smaller than n, since s contains lower alphabets
        increase lower boundary as we find smaller removal
        which is slow since we are depth first traverse and exploring potentially invalid branches
        '''
        start = time.time()
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
        end = time.time()
        print(end-start)
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
t = '()'
t = '())'
t = '()a)'
t = '(())a))'
r = Solution().removeInvalidParentheses(t)
print(r)
