class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        '''
        stack
        for every step convert to int
        14min+debug7min
        t:O(n)
        s:O(n)
        '''

        stack = []
        idx = 0
        n = len(tokens)
        while idx < n:  # or for token in tokens
            cur = tokens[idx]
            idx += 1
            if cur[-1].isdigit():  # minus number
                stack.append(int(cur))
            else:
                b = stack.pop()
                a = stack.pop()
                if cur == '+':
                    stack.append(a+b)
                elif cur == '-':
                    stack.append(a-b)
                elif cur == '*':
                    stack.append(a*b)
                elif cur == '/':
                    stack.append(int(a/b))
        return stack[0]


t = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
r = Solution().evalRPN(t)
print(r)
