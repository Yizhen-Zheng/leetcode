class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        '''
        initial thought:
        (ord(c)-ord(a))%26, then it's thread of c
        sum of each threads(should be unique)
        use set to find each longest threads
        then combination each threads(maybe use memorization for factorial)
        how many combination n we can find with len = l thread:
        n = 2**(l-1)
        'abca','abcab',: the second 'a' should be ignored for duplicated calculation
        'abcbc': the second 'bc' should be ignored
        'abcza': the second a should be kept
            threads = set()
            def is_thread(idx) -> bool:
                if ord(s[idx]) == ord(s[idx-1])+1 or (s[idx-1] == 'z' and s[idx] == 'a'):
                    return True
                return False
            end = 0
            while end < len(s):
                start = end
                while end < len(s) and is_thread(end):
                    end += 1
                threads.add(s[start:end])
                ...(Don't know how to write furthur)

        after:
        abc: 
        from a back to start: 1 char -> a can form 1 substr(a)
        from b back to start: 2 char -> b can form 2 substr(ab, b)
        from c back to start: 3 char -> c can form 3 substr(abc, bc, c)...
        '''
        dp = [0]*26
        max_len = 0
        for i in range(len(s)):
            char_idx = ord(s[i])-ord('a')
            if i > 0 and (ord(s[i-1])+1 == ord(s[i]) or ord(s[i-1]) == ord(s[i])+25):
                max_len += 1
            else:
                max_len = 1
            dp[char_idx] = max(dp[char_idx], max_len)
        print(dp)

        return sum(dp)


# t = 's'
# t = 'ab'
# t = 'sbc'
# t = 'abf'
# t = 'aba'
# t = 'ada'
t = 'zacd'

r = Solution().findSubstringInWraproundString(t)
print(r)
