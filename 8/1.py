class Solution:
    def myAtoi(self, s: str) -> int:
        '''
        ord 0 = 48
        ord 9 = 57
        if find multiple sign, exit loop  
        24min
        debug: 25min
        '''
        prev = None
        sign = 1
        res = 0
        for char in s:
            if 48 <= ord(char) <= 57:
                res = res*10+int(char)
                prev = int(char)

            elif prev == None and char == '-':
                sign = -sign
                prev = char
            elif prev == None and char == '+':
                prev = char
                continue
            elif prev == None and char == ' ':
                continue
            else:
                break

        res *= sign

        if res > ((1 << 31)-1):
            return (1 << 31)-1
        if res < (-(1 << 31)):
            return -(1 << 31)
        return res

    def myAtoi(self, s: str) -> int:
        '''
        lstrip: remove leading char
        isdigit: if str is number 
        '''
        s = s.lstrip()
        prev = None
        sign = 1
        res = 0
        for char in s:
            if char.isdigit():
                res = res*10+int(char)
                prev = int(char)
            elif prev == None and char == '-':
                sign = -sign
                prev = char
            elif prev == None and char == '+':
                prev = char
                continue
            else:
                break

        res *= sign
        if res > ((1 << 31)-1):
            return (1 << 31)-1
        if res < (-(1 << 31)):
            return -(1 << 31)
        return res


t = ''
t = '+-  42'
# t = '0-1'
# t = 'a'
# t = "words and 987"
# t = "2147483646"
r = Solution().myAtoi(t)
print(r)
