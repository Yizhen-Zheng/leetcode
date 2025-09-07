class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        '''
        review
        7:54-8:06
        13min
        brute-force
        t: O(n^2)(for every start position,it has approximately n children, each children multiply n) 
        s: O(n)(trie height)

        '''
        wordDict = set(wordDict)
        n = len(s)

        def dfs(start):
            if start >= n:
                return True
            res = False
            for end in range(start, n):
                if s[start:end+1] in wordDict:
                    res |= dfs(end+1)
            return res
        return dfs(0)

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        '''
        review
        8:06-8:18
        memorization
        parent problem: if can form from start 0
        subproblem: can form from start n and can form previously
        t: O(n**2) 
        s: O(n)(both dp and stack depth)
        why this not work: we may visit same start position and calculate multiple times
        '''
        wordDict = set(wordDict)
        n = len(s)
        memo = [None]*n

        def dfs(start):
            if start >= n:
                return True
            if memo[start] is not None:
                return memo[start]
            res = False
            for end in range(start, n):
                if s[start:end+1] in wordDict:
                    res |= dfs(end+1)
                if res:
                    break
            memo[start] = res
            return res
        return dfs(0)

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        '''
        solution
        seems first is dummy(if word does not exist, we've always visited it)
        '''
        n = len(s)
        visited_segments = [False]*(n+1)
        visited_segments[0] = True
        min_len, max_len = float('inf'), 0
        for w in wordDict:
            min_len = min(min_len, len(w))
            max_len = max(max_len, len(w))
        wordDict = set(wordDict)
        for i in range(n):
            if visited_segments[i]:  # we can only build valid path if picked prev
                for j in range(i+min_len, min(i+max_len+1, n+1)):  # prevent out of range
                    w = s[i:j]
                    if w in wordDict:
                        visited_segments[j] = True
        return visited_segments[n]

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        '''
        try above solution
        t: O(n^2), or O(n*m)(visit a pos as start)
        s: O(n)
        essentially pruning a trie
            by telling each node 'tabu' children to visit
        '''
        n = len(s)
        min_step, max_step = len(min(wordDict, key=len)), len(max(wordDict, key=len))
        wordDict = set(wordDict)
        dp = [True] + [False]*n  # start stop when start==len
        for start in range(n):
            if dp[start]:  # path is valid(can start at current)
                for end in range(start+min_step, min(n+1, start+max_step+1)):  # slice end position
                    w = s[start:end]
                    if w in wordDict:
                        dp[end] = True  # this pos can be used as start
        return dp[-1]


t = ('leetcode', ['leet', 'code', 'aaaaaa', 'a'])
r = Solution().wordBreak(t[0], t[1])
print(r)
