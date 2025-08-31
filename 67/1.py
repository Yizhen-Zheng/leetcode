class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        11:13-12:00
        47min
        '''
        a, b = (list(a), list(b)) if len(a) >= len(b)else (list(b), list(a))
        b = ['0']*(len(a)-len(b))+b
        carry = '0'
        for i in range(len(a)-1, -1, -1):
            cur_a, cur_b = a[i], b[i]
            if cur_a == '1' and cur_b == '1':
                a[i] = carry  # cur is prev carry
                carry = '1'
            elif cur_a == '0' and cur_b == '0':
                a[i] = carry  # add prev carry to cur digit
                carry = '0'  # clear carry
            else:  # one of them is 1
                # if carry==1, cur digit and carry will be unchanged
                if carry == '0':
                    a[i] = '1'
                else:
                    a[i] = '0'
        if carry == '1':
            return ''.join([carry]+a)
        else:
            return ''.join(a)

    def addBinary(self, a: str, b: str) -> str:
        '''
        solution:

        '''
        s = []
        carry = 0
        i = len(a)-1
        j = len(b)-1
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1

            # if carry is 0 or 2 -> 0, 1 -> 1
            s.append(str(carry % 2))
            # carry == 2, need keep carry to next digit
            carry //= 2
        return ''.join(reversed(s))


t = ('11', '1')
t = ('1010', '1011')
# t = ('10', '1')
r = Solution().addBinary(t[0], t[1])
print(r)
