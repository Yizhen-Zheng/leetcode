class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        BF: O(n**2)(2 loop + set)
        pick/not pick?
        t:O(n)
        s:O(n)
        20 min ish?
        '''
        ans = 0
        pos = {}
        cur = 0
        for i, char in enumerate(s):
            if char not in pos or pos[char] < i-cur:
                cur += 1
            else:
                # ?
                cur = i-pos[char]  # throw old(i,e, moving left ptr in O(1) time)
            pos[char] = i
            ans = max(ans, cur)  # <---need to update after loop(in case only one char!!!)

        return ans


t = " "
r = Solution().lengthOfLongestSubstring(t)

print(r)
