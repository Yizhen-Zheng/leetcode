class Solution:
    def calculate(self, s: str) -> int:
        '''
        simple calculator
        parse in O(n) time
        8min+10min+debug20min = 48min
        t:O(n)
        s:O(n)
        '''
        def read_token(s: str):
            tokens = []
            i = 0
            while i < len(s):
                char = s[i]
                if char in '+-()':
                    tokens.append(char)
                    i += 1
                elif char == ' ':
                    i += 1
                num = 0
                while i < len(s) and s[i].isdigit():
                    num *= 10
                    num += int(s[i])
                    i += 1
                tokens.append(num)
            return tokens

        def evaluate(tokens: list, idx):
            operation = None
            res = 0
            while idx < len(tokens):
                cur = tokens[idx]
                if cur == '(':
                    cur, idx = evaluate(tokens, idx+1)
                if isinstance(cur, int):
                    if operation != '-':
                        res = res+cur
                    else:
                        res = res-cur
                if cur == '-' or cur == '+':
                    operation = cur
                elif cur == ')':
                    return res, idx
                idx += 1
            return res
        tokens = read_token(s)
        return evaluate(tokens, 0)

    def calculate(self, s: str) -> int:
        '''
        try eval in one run
        t:O(n)
        s:O(m)(parenthesis number)
        '''

        def evaluate(tokens: str, idx):
            operation = None
            res = 0
            while idx < len(tokens):
                if tokens[idx] == ' ':  # skip white space
                    idx += 1
                elif tokens[idx] == '(':  # eval inner tokens
                    cur_right, idx = evaluate(tokens, idx+1)
                    if operation != '-':
                        res = res+cur_right
                    else:
                        res = res-cur_right
                    idx += 1
                elif tokens[idx] == ')':  # inner eval finish
                    return res, idx
                elif tokens[idx] == '-' or tokens[idx] == '+':  # operator
                    operation = tokens[idx]
                    idx += 1
                else:  # digit
                    num = 0
                    while idx < len(tokens) and tokens[idx].isdigit():  # read whole number
                        num *= 10
                        num += int(s[idx])
                        idx += 1
                    if operation != '-':
                        res = res+num
                    else:
                        res = res-num
            return res
        return evaluate(s, 0)

    def calculate(self, s: str) -> int:
        '''
        stack
        it's flatten structure as always converting 'local' operator into correct global mean
        '''
        stack = [1]
        idx = 0
        cur_number = 0
        res = 0
        operator = 1
        while idx < len(s):
            if s[idx].isdigit():  # it's in reading number
                cur_number *= 10
                cur_number += int(s[idx])
            elif s[idx] == '(':
                stack.append(operator)  # store scope operator
            elif s[idx] == ')':
                stack.pop()  # remove finished operator
            elif s[idx] == '+' or s[idx] == '-':
                # apply prev operator
                res += cur_number*operator
                # read literal val
                cur_operator = 1 if s[idx] == '+'else -1
                # mask new operator with scope operator, always use 'absolute' correct one
                operator = cur_operator*stack[-1]
                # reset cur num in processing
                cur_number = 0
            else:
                # idx+=1
                # continue
                pass
            idx += 1
        res += cur_number*operator  # add tail number
        return res


t = '1 + 1'
t = '1 + (-1)'
t = '(1 + (-1)-(2-2))'
r = Solution().calculate(t)
print(r)
