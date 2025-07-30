class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        '''
        make combination without duplication
        small size(input len <=4)
        can use a set, 2^n
        keep order of nums
        23min
        seems no need to check unique?
        - decision tree no overlapping (each digit represents char that not duplicate with others)
        this is a BFS(process each layer, then go next)
        t: O(2^n), n is len(s)(n*2^n / 2)
        s: O(2^n)(combination: 3*3*4*...)
        '''
        if not digits:
            return []
        num_to_char = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        n = len(digits)
        ans = [[]]
        for i in range(0, n):
            cur_num = digits[i]
            cur_layer = []  # like a queue
            for elem in ans:  # for each existing
                for char in num_to_char[cur_num]:
                    cur_layer.append(elem+[char])
            ans = cur_layer
        return list(map(lambda x: ''.join(x), ans))

        unique = set()
        # print(list(map(lambda x: ''.join(x), ans)))
        for elem in ans:
            unique.add(''.join(elem))
        return list(unique)

    def letterCombinations(self, digits: str) -> list[str]:
        '''
        DFS
        '''
        if not digits:
            return []
        num_to_char = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        ans = []

        def rec(ans, cur_ans, idx, s):
            if idx >= len(s):
                ans.append(cur_ans)
                return

            for elem in num_to_char[s[idx]]:
                rec(ans, cur_ans+[elem], idx+1, s)
            return ans

        rec(ans, [], 0, digits)
        return list(map(lambda x: ''.join(x), ans))

    def letterCombinations(self, digits: str) -> list[str]:
        '''
        BFS, actually same as 1st
        '''
        if not digits:
            return []
        num_to_char = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        n = len(digits)
        ans = [[]]
        for i in range(n):
            temp = []
            for char in num_to_char[digits[i]]:
                for path in ans:
                    temp.append(path+[char])
            ans = temp

        return list(map(lambda x: ''.join(x), ans))

    def letterCombinations(self, digits: str) -> list[str]:
        '''DFS, stack'''
        if not digits:
            return []
        num_to_char = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        n = len(digits)
        ans = []
        stack = [[]]
        while stack:
            path = stack.pop()
            if len(path) == n:
                ans.append(''.join(path))
                continue
            digit = digits[len(path)]
            for char in num_to_char[digit]:
                stack.append(path+[char])
        return ans


t = '22'
t = '222'
r = Solution().letterCombinations(t)
print(r)
