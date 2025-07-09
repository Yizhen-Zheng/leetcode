from typing import List
import time


class Solution:

    def removeInvalidParenthesesI(self, s: str) -> List[str]:
        '''
        num of parentheses may smaller than n, since s contains lower alphabets
        increase lower boundary as we find smaller removal
        breadth first traverse
        which is still slow 
        FIFO: pruning
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

    def removeInvalidParentheses(self, s: str) -> List[str]:
        '''
        num of parentheses may smaller than n, since s contains lower alphabets
        increase lower boundary as we find smaller removal
        breadth first traverse
        FIFO: pruning
        this one works
        this looks fast on my local

        '''

        parentheses = s
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
        perms = set()
        while idx < len(q):
            cur = q[idx]
            idx += 1
            if len(cur) < lower_boundary:
                continue
            if check(cur):
                lower_boundary = max(lower_boundary, len(cur))
                res.add(cur)  # prevent duplicated, exit this branch
            for i in range(len(cur)):
                if not (ord('a') <= ord(cur[i]) <= ord('z')):
                    newp = cur[:i]+cur[i+1:]

                    if newp not in perms:
                        q.append(newp)
                        perms.add(newp)

        return list(res)


t = ''
t = '()'
t = '())'
t = '()a)'
t = '(())a))'
t = "()())()"
t = "()())()))e))))"
# t = "()(((((((((((((e)"

start = time.time()
r = Solution().removeInvalidParentheses(t)
end = time.time()
print(end-start)
print(r)
