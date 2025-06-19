from collections import defaultdict


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        actually we need all the combination(following relative order) of the str we search
        basic recursion:
        O(2^n)
        just check all the combinations (for each s[i], do we use this char or throw this away?)
        so we form a tree, if the 2 current_char are not equat, either throw away text1[current] or text2[current]
        then we can observe that we have many duplicated sub-tree which causes repeated calcupation
        so we can try DP to memorization those 
        why not 2 pointer: 
        each char(to keep or to throw away) is independent from it's prev and next. 
        so 2 pointer won't work for absence of monotonicity(i think, 25/06/18)
        (or maybe monotonicity is just one use case of 2 pointer)
        '''
        m = len(text1)
        n = len(text2)

        def rec(i1, i2):
            '''
            base cases:
            ('', remian), or  (remian, '')
            check if 2 str have substr -> check if substrs have substr ->
            if a char is substr of another str -> if a char equal to another(basic substr)
            '''
            if i1 > m-1 or i2 > n-1:
                return 0
            if text1[i1] == text2[i2]:
                return (1 + rec(i1+1, i2+1))
            else:
                a = rec(i1, i2+1)
                b = rec(i1+1, i2)
                return max(a, b)

        return rec(0, 0)


# t = ('', '')
# t = ('abcde', 'ace')
# t = ('afcde', 'oze')
t = ('erb', 'rbde')
t = ('errb', 'rbde')
# t = ('afcdae', 'azf')
# t = ('aezzzzzz', 'azfzfz')
# t = ('aez', 'aze')
r = Solution().longestCommonSubsequence(t[0], t[1])
print(r)
