from collections import defaultdict


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        brute force: recursion -> stack
        '''
        m = len(text1)
        n = len(text2)

        stk = [(0, 0, 0)]
        lcs = 0
        while stk:
            i, j, count = stk.pop()
            if i > m-1 or j > n-1:
                lcs = max(lcs, count)
                # don't break here, buz there might be ramaining ones in stack
                continue
            if text1[i] == text2[j]:
                count += 1
                stk.append((i+1, j+1, count))
                continue
            stk.append((i, j+1, count))
            stk.append((i+1, j, count))

        return lcs


# t = ('', '')
# t = ('abcde', 'ace')
# t = ('afcde', 'oze')
# t = ('erb', 'rbde')
# t = ('errb', 'rbde')
t = ('afcdae', 'azf')
# t = ('aezzzzzz', 'azfzfz')
# t = ('aez', 'aze')
# t = ("bsbininm", 'jmjkbkjkv')
r = Solution().longestCommonSubsequence(t[0], t[1])
print(r)
