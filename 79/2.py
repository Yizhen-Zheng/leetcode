
from collections import Counter


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        '''
        a more efficient way:
        with dfs we can temprary change origin grid
        i think we can also do this with stack, record what should change back when we pop the stack
        '''
        # check number of chars:

        if Counter(word)-Counter(char for row in board for char in row):
            return False
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m = len(board)
        n = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = '#'

            found = False
            for nextr, nextc in directions:
                found = found or dfs(r+nextr, c+nextc, i+1)

            board[r][c] = temp
            return found

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False


# t = ([['A']], 'A')
# above not work,
# Traceback (most recent call last):
#   File "/Users/abcd/CodeProject/practice/LeetCode/79/2.py", line 46, in <module>
#     r = Solution().exist(t[0], t[1])
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/abcd/CodeProject/practice/LeetCode/79/2.py", line 37, in exist
#     if board[r][c] == word[0] and dfs(r, c, 0):
#                                   ^^^^^^^^^^^^
#   File "/Users/abcd/CodeProject/practice/LeetCode/79/2.py", line 26, in dfs
#     board[r][c] = '#'
#     ~~~~~~~~^^^
# TypeError: 'str' object does not support item assignment
t = ([['A']], 'B')
# t = ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCCED')
# t = ([["A", "B", "C", "C"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCCED')
r = Solution().exist(t[0], t[1])

print(r)

'''
one line nested for in:
        for outer_v in outer_iterable for inner_v in inner_iterable
        [print(char) for row in board for char in row]

        note: dict cannot built-in subtraction
        Counter subtraction:
        1. Using the subtract() method:
            The subtract() method modifies the Counter object in-place by subtracting counts from another iterable or mapping.
            It preserves zero and negative values, unlike the - operator.

            from collections import Counter
            counter1 = Counter({'a': 4, 'b': 2, 'c': 1})
            counter2 = Counter({'a': 1, 'b': 3, 'd': 2, 'e': 3})
            counter1.subtract(counter2)
            print(counter1)  # Output: Counter({'a': 3, 'b': -1, 'c': 1, 'd': -2, 'e': -3})

        2. Using the - operator:
            The - operator creates a new Counter object with the result of subtracting the second Counter from the first.
            It removes keys with zero or negative counts.

        word[::-1]: reverse string (use string slicing, begin, end, step-size)
'''
