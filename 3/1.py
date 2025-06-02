class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return s.length
        lookup = dict()
        # pointer to index
        l = 0
        r = 0
        longest = ''
        while r < len(s):
            if s[r] in lookup.keys():
                # move , while l < lookup[s[r]]+1, l move, remove items from lookup
                duplicate_char_idx = lookup[s[r]]+1
                while l < duplicate_char_idx:
                    del lookup[s[l]]
                    l += 1
            # move left pointer
            # ?: substring.includes: actually O(N); using obj for O(1)
            current_len = r-l+1
            if current_len >= len(longest):
                longest = s[l:r+1]
            # store right most char and its index
            lookup[s[r]] = r
            r += 1
        return longest


t1 = 'abdceb'
# idx:
# 0-1-3-2-4-2
s = Solution().lengthOfLongestSubstring(t1)
print(s)
