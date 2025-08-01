class Solution:
    def isValid(self, s: str) -> bool:
        '''
        have multiple kinds of parentheses
        recursion,
        stack,
        2-ptr
        15min + debug1min
        t:O(n)
        s:O(n)(store left)
        '''
        n = len(s)
        left = ['(', '{', '[']
        stack = []
        for i in range(n):
            cur = s[i]
            if cur in left:
                stack.append(cur)
            elif stack:
                pair = stack.pop()
                if (pair == '[' and cur != ']'):
                    return False
                elif (pair == '{' and cur != '}'):
                    return False
                elif (pair == '(' and cur != ')'):
                    return False
            else:
                return False
        return True if not stack else False

    def isValid(self, s: str) -> bool:
        '''a concise version of stack'''
        pair = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            if char in pair:
                stack.append(char)
                continue
            if not stack or pair[stack.pop()] != char:
                return False

        return not stack

    def isValid(self, s: str) -> bool:
        '''rec'''
        n = len(s)
        pair = {'(': ')', '{': '}', '[': ']'}

        def rec(path: list):
            if not path:
                return True
            if path[0] not in pair:
                return False
            opening = path[0]
            closing = pair[opening]
            depth = 0
            for i in range(len(path)):
                if path[i] in pair:
                    depth += 1
                elif path[i] in pair.values():
                    depth -= 1
                if depth == 0:
                    if path[i] != closing:
                        return False
                    return rec(path[1:i]) and rec(path[i+1:])
            return False
        return rec(list(s))

    def isValid(self, s: str) -> bool:
        '''
        rec
        we know whatever closing is returned, there should be an opening to 'receive' this
        if opening follows a prev opening, go to next layer recursion
        '''
        n = len(s)
        pair = {'(': ')', '{': '}', '[': ']'}

        def rec(idx):
            if idx >= n:
                return idx
            # return closing
            if s[idx] not in pair:
                return idx
            opening = s[idx]
            closing = pair[opening]
            next_idx = rec(idx+1)  # retrived pair
            if next_idx < 0 or next_idx > n-1 or s[next_idx] != closing:
                return -1
            return rec(next_idx+1)

        return rec(0) == len(s)


t = '[{}]'
t = '[]{}'
t = '[]}'
t = '}{}'
t = '[[]'
t = "({{{{}}}))"
# t = "({{{}}))"
# t = '[[]]]'
r = Solution().isValid(t)
print(r)
