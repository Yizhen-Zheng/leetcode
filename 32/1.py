class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        use a stack, initially it's left-modt-valid-range is -1(if we find '()', it's valid range if [0,1], so i-(-1) gives 2)
        if we have paris of '()'s, it should be eventually taken out of idxed except the boundaries(the last seen invalid)
        e.g.
        : in '((()', the first 2 '(' will be left in the stack bcz no ')' will pari them
        so the boundary will natually be 1
        : in '())))(())', from idx=2, it starts to push itself to be the new valid-boundary
        idx[2,3,4]: every ')' checks and find nothing, and push itself 
            (means if it's left in the stack latter(for sure bcz no left will pair it), 
            it marks the invalid and the start point of new valid threads)
            for this reason, if we find a valid pair, we check the left elements and tell currently how far it can form valid threads

        '''
        idxes = [-1]
        # a stack to store found '(' initially
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                idxes.append(i)
            else:
                # if current is ')'
                idxes.pop()
                if not idxes:
                    # means ')' is more than '(' we've found
                    # ))(), ()))
                    idxes.append(i)
                else:
                    max_len = max(max_len, i-idxes[-1])

        return max_len


# t = '('
# t = ')'
# t = ''
# t = '))()'
# t = '((()))'
# t = '()((()'
t = '())()())))'
r = Solution().longestValidParentheses(t)
print(r)
