class Solution:
    '''
    brute force: check all perms(iterate). O(n^3)
        for s in (0,n): 
            for e in (s,n):
                check(s,e)
    BF 2.0: O(n^2)
        for center in (0,n):
            expand_to_side
    '''

    def longestPalindrome(self, s: str) -> str:
        '''
        try review
        8:20-
        brute force: just expand from all
        idea: utilize the symmetry
        works!
        '''
        center = 0
        ss = '#'+'#'.join(s)+'#'
        print(ss)
        n = len(ss)
        max_len = [0]*n
        longest_center = 0

        for i in range(1, n):
            center_radius = max_len[center]
            symmetry_len_can_use = 0
            if (i-center) <= center_radius:
                symmetry_idx = center-(i-center)
                center_boundary = center-center_radius
                symmetry_len_can_use = min(symmetry_idx-center_boundary, max_len[symmetry_idx])
                max_len[i] = symmetry_len_can_use

            l, r = i-symmetry_len_can_use-1, i+symmetry_len_can_use+1
            while l > -1 and r < n and ss[l] == ss[r]:
                l -= 1
                r += 1
                max_len[i] += 1
            # update center if cur right bound > center right bound
            if max_len[i]+i > max_len[center]+center:
                center = i
            if max_len[i] > max_len[longest_center]:
                longest_center = i
        print(max_len)
        ans = ss[longest_center-max_len[longest_center]:longest_center+max_len[longest_center]+1]
        ans = ans.replace('#', '')
        return ans


t = ''
# t = 'a'
t = 'abc'
t = 'abab'
# t = 'abcec'
t = 'aacabdkacaa'
t = "bacabab"
r = Solution().longestPalindrome(t)
print(r)
