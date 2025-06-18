from collections import Counter


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        '''
        a more efficient way:
        with dfs we can temprary change origin grid
        stack version, record what should change back when we pop the stack
        '''
        # check number of chars:

        if Counter(word)-Counter(char for row in board for char in row):
            return False
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m = len(board)
        n = len(board[0])

        def dfs(r, c):
            stack = [(r, c, 0, board[r][c], 'explore')]
            while stack:
                r, c, word_idx, origin_char, action = stack.pop()
                if action == 'explore':
                    board[r][c] = '#'
                    if word_idx == len(word)-1:
                        return True
                    stack.append((r, c, word_idx, origin_char, 'backtrack'))
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if nr >= 0 and nc >= 0 and nr < m and nc < n and board[nr][nc] == word[word_idx+1]:
                            stack.append((nr, nc, word_idx+1, board[nr][nc], 'explore'))
                elif action == 'backtrack':
                    board[r][c] = origin_char
            return False

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(r, c):
                    return True
        return False


t = ([['A']], 'A')

# t = ([['A']], 'B')
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
