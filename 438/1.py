class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        '''
        anagram: any order(not paralindrome)
        brute-force: dfs
        t: O(n**m)(from each start in s, need check len(p))
        s: O(m)(stack depth)
        16:18-16:34
        '''
        chars = [0]*26
        A = ord('a')
        for c in p:
            chars[ord(c)-A] += 1
        n, m = len(s), len(p)

        # check each char in s
        def dfs(cur_idx: int, todo: int):
            if todo == 0:
                return True
            if cur_idx >= n:
                return False
            cur_char = s[cur_idx]
            res = False
            if chars[ord(cur_char)-A] > 0:  # need to do
                chars[ord(cur_char)-A] -= 1
                res = dfs(cur_idx+1, todo-1)
                chars[ord(cur_char)-A] += 1

            return res
        ans = []
        for start in range(0, n):
            can_form = dfs(start, m)
            if can_form:
                ans.append(start)
        return ans

    def findAnagrams(self, s: str, p: str) -> list[int]:
        '''
        try optimize:
        sliding window(window size: m)
        need to know first and last char
        20:45-21:20 35min
        t: O(n)
        s: O(n)
        why it works:
        s='baab', p='aa', n=4, m=2
        [2,0,...]
        in_idx=0: [2,-1,...], remain=2
        in_idx=1: [1,-1,...]  remain=1
        in_idx=2, out_idx=0: [0,0,...] remain=0, add to ans
        in_idx=3, out_idx=1: [1,-1,...] remain=1
        the unneeded char won't go above 0
        if we 'turn back' a necessary char, its value becomes positive
        so when 'turning back', just check if val>0, and increment remain

        another example:
        s='aab', p='ab'
        [1,1,...]
        in_idx=0: [0,1,...], remain=1
        in_idx=1: [-1,1,...], remain=1
        in_idx=2, out_idx=0: [0,0,...] remain=0, add to ans

        similarly, if we have a redundancy of a necessary val, it also becomes negative
        and when 'turning back', we just first remove that redundant part
        and 'remain' will only be increased if all 'redundancy' has been used
        '''
        todo = [0]*(ord('z')+1)
        for c in p:
            todo[ord(c)] += 1
        n, m = len(s), len(p)
        if m > n:
            return []
        remain = m
        ans = []
        back = 0
        for front in range(0, n-m+1):
            if front > 0:
                todo[ord(s[front-1])] += 1
                if todo[ord(s[front-1])] > 0:
                    remain += 1
            while back-front < m:
                todo[ord(s[back])] -= 1
                if todo[ord(s[back])] >= 0:
                    remain -= 1
                back += 1
            if remain == 0:
                ans.append(front)
        return ans

    def findAnagrams(self, s: str, p: str) -> list[int]:
        '''
        the idea: 
        window-out --
        window-in ++
        compare 2 status(if counter_cur(the window in s) == counter_goal(Counter(p)))
        '''
        todo = [0]*(ord('z')+1)
        for c in p:
            todo[ord(c)] += 1
        n, m = len(s), len(p)
        if m > n:
            return []
        remain = m
        ans = []
        for i in range(0, n):
            if i >= m:  # need to remove emel goes out of window
                todo[ord(s[i-m])] += 1
                if todo[ord(s[i-m])] > 0:  # if it's needed elem
                    remain += 1
            todo[ord(s[i])] -= 1
            if todo[ord(s[i])] >= 0:
                remain -= 1
            if remain == 0:
                ans.append(i-m+1)
        return ans

    def findAnagrams(self, s: str, p: str) -> list[int]:
        '''
        another approach is build 2 map:
        goal(conuter_p)
        cur(counter_current_substr)
        by doing this we don't need to check if increment remain_count(handle the unneeded char)
        '''
        n, m = len(s), len(p)
        if m > n:
            return []
        p_counter, s_counter = [0]*(ord('z')+1), [0]*(ord('z')+1)
        for c in p:
            p_counter[ord(c)] += 1
        ans = []
        for i in range(n):
            if i >= m:  # remove elems out of window
                s_counter[ord(s[i-m])] -= 1

            s_counter[ord(s[i])] += 1  # add elem comes in

            if s_counter == p_counter:  # compare
                ans.append(i-m+1)
        return ans


t = ('cbaebabacd', 'abc')
# t = ("abab", 'ab')
r = Solution().findAnagrams(t[0], t[1])
print(r)
