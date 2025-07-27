from collections import deque


class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        brute force: 
        until find one, try to remove chars from str, BFS
        15min
        !NOTE this should be consistent
        '''
        chars = list(s)

        def check(chars):
            for i in range(len(chars)//2):
                if chars[i] != chars[-1-i]:
                    return False
            return True
        queue = [chars]
        seen = set()
        seen.add(s)
        idx = 0
        while idx < len(queue):
            cur = queue[idx]
            if check(cur):
                return ''.join(cur)
            for i in range(len(cur)):
                if i == 0 or cur[i] != cur[i-1]:
                    queue.append(cur[:i]+cur[i+1:])
            idx += 1

    def longestPalindrome(self, s: str) -> str:
        '''
        pick current and all prev, or start a new one from current
        brute force: 
        BFS(TLE)
        from the whole str, cut 2 sides gradually
        45min
        '''
        chars = list(s)

        def check(chars, s, e):
            # print(s, e)
            if s >= e:
                return True
            for i in range(0, (e-s+1)//2):
                if chars[s+i] != chars[e-i]:
                    return False
            return True

        n = len(chars)
        seen = set()

        def rec(chars, seen, s, e):
            # print(chars[s:e+1])
            if check(chars, s, e):
                return (s, e)
            news1 = newe1 = news2 = newe2 = -1
            if (s+1, e) not in seen:
                news1, newe1 = rec(chars, seen, s+1, e)  # remove_left
                seen.add((s+1, e))
            if (s, e-1) not in seen:
                news2, newe2 = rec(chars, seen, s, e-1)  # remove_right
                seen.add((s, e-1))
            if (newe1-news1) > (newe2-news2):
                return (news1, newe1)
            else:
                return (news2, newe2)
        s, e = rec(chars, seen, 0, n-1)
        if s != -1 and e != -1:
            return ''.join(chars[s:e+1])
        else:
            return ''

    def longestPalindrome(self, s: str) -> str:
        '''
        pick current and all prev, or start a new one from current
        brute force: 
        BFS
        15min
        from each position, expand to 2 sides
        or from the whole str, cut 2 sides gradually
        NOTE i got the big O wrong(i thought it was t: O(2^n) and s:O(nlogn))
        time:O(n^3) 
            enumerate s and e: O(n^2)
            check: O(n)

        s:O(n^2)
            seen: O(n^2)(all combination of s and e)
            q: 
            layer0: 1 elem
            layer2: 2 elem(0, n-1),(1,n)
            ...
            layer n-1: n-1 elem (0,1),(1,2),...(n-2,n-1),(n-1,n)
            layer n: n elem (0,0),(1,1),...(n-1,n-1),(n,n) 
        '''
        chars = s

        def check(chars, s, e):
            # print(s, e)
            if s >= e:
                return True
            for i in range(0, (e-s+1)//2):
                if chars[s+i] != chars[e-i]:
                    return False
            return True

        n = len(chars)
        q = deque([(0, n-1)])
        seen = set()
        while q:
            s, e = q.popleft()
            if check(chars, s, e):
                break
            s1, e1 = s+1, e
            s2, e2 = s, e-1
            if (s1, e1)not in seen:
                seen.add((s1, e1))
                q.append((s1, e1))
            if (s2, e2)not in seen:
                seen.add((s2, e2))
                q.append((s2, e2))

        return chars[s:e+1]

    def longestPalindrome(self, s: str) -> str:
        '''
        from each position, expand to 2 sides
        t: O(n)
        s: O(1)
        '''
        longest = ''

        def expand(s, l, r):
            n = len(s)
            while l > -1 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l+1, r-1
        n = len(s)
        for i in range(0, n):
            odd_l, odd_r = expand(s, i, i)
            even_l, even_r = expand(s, i, i+1)
            # compare len:
            if odd_r-odd_l+1 > len(longest):
                longest = s[odd_l:odd_r+1]
            if even_r-even_l+1 > len(longest):
                longest = s[even_l:even_r+1]
        return longest

    def longestPalindrome(self, s: str) -> str:
        '''
        since there're 2 variables(s,e),try dp
        row: center
        col: right len
        idx: i//2, odd idx: 2 side
        why
                dp[i] = min(right-i, dp[center-(i-center)])
        example1:
        #c#b#c#b#a#
             c ir
           3 3 1
        although i's mirror has 3, it cannot go beyond the right border

        example2:
        a c a b a c a b a
        1 1 1 7 1 5 1 1 1
                  c.  i r
        although i's mirror has 7, it cannot go beyond the right border

        '''

        modified = '#'+'#'.join(list(s))+'#'
        dp = [0]*len(modified)
        center = 0
        right = 0
        max_len = 0
        max_str = ''
        for i in range(len(modified)):
            if i < right:
                # within old max's territory, reuse prev res
                dp[i] = min(right-i, dp[center-(i-center)])

            while i-dp[i]-1 >= 0 and i+dp[i]+1 < len(modified) and modified[i-dp[i]-1] == modified[i+dp[i]+1]:
                # dp value: single direction expanding distance
                # e,g, '#a#b#a#' on b:expand val is 3, on a: expand 1
                # by including the sharp mark, we generalize odd and even palindrome
                dp[i] += 1
            if i+dp[i] > right:
                center = i
                right = i+dp[i]
            if dp[i] > max_len:
                max_len = dp[i]
                # why slice like this?
                max_str = modified[i-dp[i]:i+dp[i]+1].replace('#', '')
        return max_str


t = ''
# t = 'a'
# t = 'abc'
t = 'abcec'
# t = 'aacabdkacaa'
r = Solution().longestPalindrome(t)
print(r)
