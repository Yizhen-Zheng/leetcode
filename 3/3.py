from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        review
        6:58-7:50
        brute force:
        n*n, then find max
        '''
        longest = 0
        n = len(s)
        for start in range(n):
            for end in range(start, n):
                seen = set()
                for cur in range(start, end+1):
                    if s[cur] in seen:
                        break
                    seen.add(s[cur])
                longest = max(longest, cur-start+(s[cur] not in seen))

        return longest

    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        brute force
        '''
        longest = 0
        n = len(s)
        for start in range(n):
            seen = set()
            for e in range(start, n):
                if s[e] in seen:
                    break
                seen.add(s[e])
            longest = max(longest, e-start+(s[e] not in seen))
        return longest

    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        sliding window
        7:50-8:02, debug - 8:08

        '''
        start, cur, n = 0, 0, len(s)
        m = {}
        longest = 0
        while cur < n:
            cur_char_idx = ord(s[cur])
            if cur_char_idx in m and m[cur_char_idx] >= start:  # in current window,find dup
                # update previous res
                longest = max(longest, cur-start)
                start = m[cur_char_idx]+1
                m[cur_char_idx] = cur
                cur += 1
            else:
                m[cur_char_idx] = cur
                cur += 1
                longest = max(longest, cur-start)

        return longest

    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        try clean up
        double while: 
            while end in dup, remove from head(in single loop,just update ptr position)
        '''
        start, cur, n = 0, 0, len(s)
        m = {}
        longest = 0
        while cur < n:
            cur_char_idx = ord(s[cur])
            if cur_char_idx in m and m[cur_char_idx] >= start:  # in current window,find dup
                # update window size
                start = m[cur_char_idx]+1
            longest = max(longest, cur-start+1)
            m[cur_char_idx] = cur
            cur += 1

        return longest


t = "abcabcbb"
# t = 'dvdf'
r = Solution().lengthOfLongestSubstring(t)
print(r)
