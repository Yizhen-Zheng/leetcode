

class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        improved version: memoization
        a-z -> 1-26
        01 is not valid

        we can roll down, keep 3 elements in memo
        '''

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

        first = 1
        second = 0
        a = is_valid(1, 1)
        b = is_valid(0, 1)

        if a == False and b == False:
            return 0
        elif not (a == True and b == True):
            second = 1
        else:
            second = 2
        idx = 2
        current = second

        while idx < len(s):

            a = is_valid(idx, idx)
            b = is_valid(idx-1, idx)

            if a == False and b == False:
                return 0
            elif a == False and b == True:
                current = first
            elif a == True and b == False:
                current = second
            else:
                current = first+second

            # only push to q if next is valid
            idx += 1
            first = second
            second = current

        return current


# t = '1'
# t = '1203'
# t = '226'
# t = '60'
# t = '10'
t = '1212121'
r = Solution().numDecodings(t)
print(r)
