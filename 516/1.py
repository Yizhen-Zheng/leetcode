class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        brute force:
        find all subsequence and return max
        2^n
        (memory / time limit)
        '''
        stk = ['']
        idx = 0
        while idx < len(s):
            new_elems = []
            for substr in stk:
                new_elems.append(substr+s[idx])
            stk.extend(new_elems)
            idx += 1

        def is_pal(str):
            for i in range(int(len(str)/2)):
                if str[i] != str[len(str)-1-i]:
                    return False
            return True
        max_len = 0
        for substr in stk:
            if (is_pal(substr)):
                max_len = max(max_len, len(substr))
        print(stk)
        return max_len

    def longestPalindromeSubseqRec(self, s: str) -> int:
        def is_pal(str):
            for i in range(int(len(str)/2)):
                if str[i] != str[len(str)-1-i]:
                    return False
            return True

        def rec(str_arr, idx):
            '''
            idx: contains current char, or not contain current char
            '''
            if idx >= len(s):
                return len(str_arr) if is_pal(str_arr) else 0

            a = rec(str_arr+[s[idx]], idx+1)
            b = rec(str_arr, idx+1)
            return max(a, b)
        r = rec([], 0)
        return r

    def longestPalindromeSubseqRecRange(self, s: str) -> int:

        def rec(l, r):
            '''
            idx: contains current char, or not contain current char
            '''
            if l > r:
                return 0
            if l == r:
                return 1
            if s[l] == s[r]:
                return 2+rec(l+1, r-1)
            return max(rec(l+1, r), rec(l, r-1))
        r = rec(0, len(s)-1)
        return r


t = ''
t = 'a'
t = 'cdd'
t = 'dded'
# t = 'ahgfghz'
# r = Solution().longestPalindromeSubseq(t)
# r = Solution().longestPalindromeSubseqRec(t)
r = Solution().longestPalindromeSubseqRecRange(t)
print(r)
