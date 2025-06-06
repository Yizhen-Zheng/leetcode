# from collections import deque


class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        intuitive version: (without memoization)
        a-z -> 1-26
        01 is not valid
        intuitive: for each num, it can branch 2 ways, so it's 2^N
        we can tabuiation or memoizaation to remember what way is valid previously 

        '''

        # this prove first is valid
        if len(s) == 1:
            return 0 if s[0] == '0' else 1

        # dq = deque([s[0]])

        def is_valid(start, end):
            if s[start] != '0' and end < len(s):
                if start == end:
                    return True
                elif end == start+1:
                    n = int(s[start]+s[end])
                    if 0 < n < 27:
                        return True
            return False

        q = []
        q_idx = 0
        count_path = 0
        if is_valid(0, 0):
            q.append((0, 0))
        if is_valid(0, 1):
            q.append((0, 1))

        while q_idx < len(q):
            start, end = q[q_idx]
            q_idx += 1
            if end == len(s)-1:
                count_path += 1
                continue
            next_start = end+1
            for i in range(0, 2):
                if is_valid(next_start, next_start+i):
                    # only push to q if next is valid
                    q.append((next_start, next_start+i))

        return count_path


# t1 = '123'
t2 = '1203'
t3 = '12349120'
t4 = '111111'
# r = Solution().numDecodings(t1)
# r = Solution().numDecodings(t2)
# r = Solution().numDecodings(t3)
r = Solution().numDecodings(t4)
print(r)
