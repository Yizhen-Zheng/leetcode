from typing import List
import time
'''
another way to set lower boundary with BFS: 
    if result is empty, means no valid seen, we can process further.
    if result has elem: an elem from at least current layer(which occurs before current) has generated result
        so any result smaller than current is invalid. 

'''


class Solution:

    def removeInvalidParenthesesI(self, s: str) -> List[str]:
        '''
        num of parentheses may smaller than n, since s contains lower alphabets
        increase lower boundary as we find smaller removal
        breadth first traverse
        which is still slow 
        FIFO: pruning

        for brute force: 
            time: 
                for each node, it has m children, and we try to remove each of them and ask if i can form a valid str
                roughly O(2^n)<-from n^n, roughly say as 2^n
            space: 
                O(n) n: len(s), as recursion depth is maximum n 
        below: both best case is O(n) (only check once and find it's done with pruning(we skip duplicated calculation))
        BFS:    
            time:
                worst case: still O(2^n) roughly, if we have '))))))' or '((((', 
            space: 
                worst case: O(n^n), since we store all seen and a manula queue
                if we use a real queue(deque), this shuold be layer breadth(cuz we pop head)
        recursion (prevent duplication version):
            time: O(2^n),roughly
            space:
                worst case: O(n) (remove all)
        to calculate time complexity thoroughly, we need:
        n! + (n-1)! + ... 1!

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

    def removeInvalidParenthesesI(self, s: str) -> List[str]:
        '''
        num of parentheses may smaller than n, since s contains lower alphabets
        increase lower boundary as we find smaller removal
        breadth first traverse
        FIFO: pruning
        this one works
        this looks fast on my local
        maybe can be further optimized
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
            if len(cur) < lower_boundary:  # prevent generating shorter ones
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

    def removeInvalidParentheses(self, s: str) -> List[str]:
        '''
            num of parentheses may smaller than n, since s contains lower alphabets
            increase lower boundary as we find smaller removal
            breadth first traverse
            FIFO: pruning
            this one works
            this looks fast on my local
            maybe can be further optimized
            '''

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

        res = []
        q = [(s, 0)]
        idx = 0
        while idx < len(q):
            cur, start_idx = q[idx]
            idx += 1
            if check(cur):
                res.append(cur)
            elif not res:
                for i in range(start_idx, len(cur)):
                    if (not (ord('a') <= ord(cur[i]) <= ord('z'))) and (cur[i] == 0 or cur[i] != cur[i-1]):
                        newp = cur[:i]+cur[i+1:]
                        q.append((newp, i))

        return res


t = ''
t = ')('
# t = '()'
# t = '())'
# t = '()a)'
# t = '(())a))'
# t = "()())()"
# t = "()())()))e))))"
# t = "()(((((((((((((e)"

start = time.time()
r = Solution().removeInvalidParentheses(t)
end = time.time()
print(end-start)
print(r)
