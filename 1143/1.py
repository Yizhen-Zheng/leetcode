from collections import defaultdict


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        without changing relative order
        brute force: (n*n)
        intuition: binary search (not work buz it's not sorted)

        if find one , then next char we only search the right of the str
        we also know t1,t2's len, one long one shhort, or equal

        subtract 2 dict?
        why this not work: sometimes we find the not best solution
        e.g.: t = ('zab', 'abzc')
        that's why we need a DP-like approach to keep each pathway indemendent

        '''
        lt, st = (text1, text2) if len(text1) > len(text2) else (text2, text1)
        ld = defaultdict(list)

        # or implement by [[] for _ in range(26)]
        for i in range(len(lt)-1, -1, -1):
            ld[lt[i]].append(i)
        # do we need s dict? not sure

        print(ld)

        best_c = 0
        for s_idx in range(len(st)):
            sub_st = st[s_idx:]
            c = 0
            l_idx = -1
            ld = defaultdict(list)
            for i in range(len(lt)-1, -1, -1):
                ld[lt[i]].append(i)
            for i in range(len(sub_st)):
                sc = sub_st[i]
                new_idx = -1
                while ld[sc] and new_idx <= l_idx:
                    new_idx = ld[sc].pop()
                if new_idx != -1 and new_idx > l_idx:
                    c += 1
                    l_idx = new_idx
            best_c = max(c, best_c)
        return best_c


# t = ('', '')
# t = ('abcde', 'ace')
# t = ('afcde', 'oze')
# t = ('oze', 'afcde')
# t = ('afcdae', 'azf')
# t = ('aezzzzzz', 'azfzfz')
# t = ('aez', 'aze')
t = ('zab', 'abzc')
t = ('"oxcpqrsvwf"', 'shmtulqrypy')
r = Solution().longestCommonSubsequence(t[0], t[1])
print(r)
'''
this not work if short has a char that long dosen't
like t = ('afcde', 'oze')
long_text, short_text = (text1, text2) if len(text1) > len(text2) else (text2, text1)
        c = 0
        s = 0
        # range of long_text we shuold search
        l = 0
        while s < len(short_text) and l < len(long_text):
            if long_text[l] == short_text[s]:
                l += 1
                s += 1
                c += 1
            else:
                l += 1

        return c
        



'''
