class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
        16:15-
        cur,center

        i misunderstood the question...
        '''
        # 16:45-16:50
        # if all can paired, return n
        # if has remain:
        #   only one remain: n
        #   otherwise, n-len(chars)+1
        chars = set()
        n = len(s)
        for c in s:
            if c in chars:
                chars.remove(c)
            else:
                chars.add(c)
        if not chars:  # all paired
            return n
        return n-len(chars)+1  # use one odd as center, others are wasted


t = "abccccdd"
r = Solution().longestPalindrome(t)
print(r)
