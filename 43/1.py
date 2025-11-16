class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        BF: 
        t: O(m*n)
        s: O(m*n)
        'manually' multiply?
        11:07-11:59
        debug: 11:59-12:06
        make sure len1>len2(otherwise will happen to add acc twice)
        80 min ish
        '''
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        if num1 == '0' or num2 == '0':
            return '0'
        ans = []
        len1, len2 = len(num1), len(num2)
        for i in range(len2-1, -1, -1):
            acc = 0
            start_dig_idx = len2-i-1
            a = int(num2[i])
            for j in range(len1-1, -1, -1):
                # from 0
                cur_dig_idx = len1-j-1 + start_dig_idx
                b = int(num1[j])
                cur = a*b+acc
                if cur_dig_idx < len(ans):  # there's something there
                    cur += int(ans[cur_dig_idx])
                acc = cur//10
                if cur_dig_idx < len(ans):  # there's something there
                    ans[cur_dig_idx] = str(cur % 10)
                else:
                    ans.append(str(cur % 10))
            # add last acc
            cur_dig_idx = len1 + start_dig_idx
            if cur_dig_idx < len(ans):  # there's something there
                ans[cur_dig_idx] = str(acc)
            else:
                ans.append(str(acc))
        if ans[-1] == '0':
            ans.pop()
        return ''.join(ans[::-1])


t = ('9', '2')
t = ('9', '99')
t = ('999', '999')
r = Solution().multiply(t[0], t[1])
print(r)
