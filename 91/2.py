

class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        intuitive version: (without memoization)
        a-z -> 1-26
        01 is not valid
        intuitive: for each num, it can branch 2 ways, so it's 2^N
        we can tabuiation or memoizaation to remember what way is valid previously 

        '''

        # this prove first is not 0

        def is_valid(start, end):
            if start >= 0 and end < len(s) and start <= end:
                if s[start] != '0' and end < len(s):
                    if start == end:
                        return True
                    elif end == start+1:
                        n = int(s[start]+s[end])
                        if 0 < n < 27:
                            return True
            return False

        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1

        memo = [0]*(len(s))
        memo[0] = 1
        a = is_valid(1, 1)
        b = is_valid(0, 1)

        if a == False and b == False:
            return 0
        elif not (a == True and b == True):
            memo[1] = 1
        else:
            memo[1] = 2
        idx = 2

        while idx < len(s):

            a = is_valid(idx, idx)
            b = is_valid(idx-1, idx)
            if a == False and b == False:
                return 0
            elif a == False and b == True:
                memo[idx] = memo[idx-2]

            elif a == True and b == False:
                memo[idx] = memo[idx-1]
            else:
                memo[idx] = memo[idx-2]+memo[idx-1]

            pass
            # only push to q if next is valid
            idx += 1
        print(memo)

        return memo[-1]


# t = '1'
# t = '1203'
# t = '226'
# t = '60'
t = '10'
# t = '1212121'
r = Solution().numDecodings(t)
print(r)
