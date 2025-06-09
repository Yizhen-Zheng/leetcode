class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        TODO: nod work currently
        str of nums, may contain *, can be 1-9
        *-> 9 ; 3*->9; *2->9+2; 2*->15; **->9+9+6
        travel from tail to head
        *num: 9 + 2 or 1 *prev (prev > 6: 1, prev < 6: 2)
        num*: 1,2: +9 or +6
        if 1, 2 + *
        '''
        if s[0] == '0':
            return 0

        cur = 0
        next = 1
        next_next = 1

        def check_ways(i):
            '''count extra ways (when 2 char can be paired)'''
            if s[i] == '*':
                # *0, *[1~6], *[7~9]
                if s[i+1] in '0123456':
                    # *0, *[1~6]
                    return next_next*2
                elif s[i+1] in '789':
                    # *[7~9]
                    return next_next
                else:
                    # *[*]
                    return next_next*15

            elif s[i] == '1':
                # 1[0~9], 1[*]
                if s[i+1] in '0123456789':
                    return next_next
                else:
                    # when 1[*]
                    return next_next*9

            elif s[i] == '2':
                # 2[0~6],2[*]
                if s[i+1] in '0123456':
                    return next_next
                elif s[i+1] == '*':
                    return next_next*6
            return 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                cur = 0
                continue
            elif s[i] == '*':
                cur = 9*next
            else:
                cur = next
            if i < len(s)-1:
                cur += check_ways(i)
            cur = cur % (1000000007)
            print(cur, ' ', next, ' ', next_next)
            next_next = next
            next = cur
            cur = 0
        return next


# t = '1*'
t = '1*203'
# t = '22*6'
# t = '*0'
# t = '10'
# t = '1212121'
r = Solution().numDecodings(t)
print(r)
