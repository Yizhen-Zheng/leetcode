class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        '''
        note it's segment, so we don't need to re-arange the words
        brute-force: for every word in dict, search in the s and if it exists, 
        split the str into xx, word, yy, then search in xx and yy
        seems can use rec, if substr is empty or exactly fit the word in wordditc, true
        question is how to split,
        enumerate split, take or of them, 
        take and of 2 parts of split
        brute-force, 9min, debug: 8min
        TLE
        t: O(2^n)
        s:rec depth: O(n)(from len to 0)

        '''
        word_dict = set(wordDict)

        def rec(word_dict, s):
            if s in word_dict:
                return True
            for i in range(1, len(s)):
                res = rec(word_dict, s[0:i]) and rec(word_dict, s[i:])
                if res == True:
                    return res
            return False

        return rec(word_dict, s)

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        '''
        memorization
        6min
        '''
        word_dict = set(wordDict)
        dp = {}

        def rec(word_dict, s, dp):
            if s in dp:
                return dp[s]
            if s in word_dict:
                dp[s] = True
                return True
            for i in range(1, len(s)):
                res = rec(word_dict, s[0:i], dp) and rec(word_dict, s[i:], dp)
                if res == True:
                    dp[s] = True
                    return res
            dp[s] = False
            return False

        return rec(word_dict, s, dp)

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        '''
        memorization, optimize to search word, not iterating all substr
        note that we can claim if a substr is valid only after checking all perms
        '''
        word_dict = set(wordDict)
        dp = {}

        def rec(word_dict, s: str, dp):
            if s in dp:
                return dp[s]
            if s in word_dict:
                dp[s] = True
                return True
            for word in word_dict:
                if s.startswith(word):
                    res = rec(word_dict, s[len(word):], dp)
                    if res:  # wait for a valid ans in loop
                        dp[s] = res
                        return res

            dp[s] = False
            return False

        return rec(word_dict, s, dp)

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        '''
        consider word='abc', dict=['ab','abc'],
        we should know abc before asserting c is invalid
        consider word='abcd', dict=['ab','abc','cd'],
        use 'ab','cd' instead of 'abc'
        so we cannot just match directly
        t:O(n^2), explore all perms(len(s)^2/2)
        s:O(n)(store if valid ends on current idx

        '''
        n = len(s)
        word_dict = set(wordDict)
        dp = [False]*(n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i-1, -1, -1):
                if dp[j]:  # only slice at end of previous valid position
                    word = s[j:i]
                    if word in word_dict:
                        dp[i] = True
                        break
        print(dp)
        return dp[n]

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        '''
        another buttom up
        t:O(n*2)(len(s)*len(word))
        seems slower than above, maybe because dict is large
        s:O(n)
        '''
        n = len(s)
        word_dict = set(wordDict)
        dp = [False]*(n+1)
        dp[0] = True  # start at empty if valid
        # i: next after prev ends
        for i in range(1, n+1):
            if dp[i-1]:  # only check if it follows a valid idx
                for word in word_dict:
                    if s[i-1:i+len(word)-1] == word:
                        # if s.startswith(word, i-1):
                        dp[i+len(word)-1] = True

        print(dp)
        return dp[-1]


t = ('', [''])
t = ('apple', ['app', 'le'])
t = ('apple', ['ap', 'le'])
# t = ('cats', ['cat', 'cats'])
r = Solution().wordBreak(t[0], t[1])
print(r)
