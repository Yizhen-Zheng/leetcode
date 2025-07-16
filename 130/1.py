from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        detect surronding, and modify anything inside border
        O on border of matrix must be false
        BFS to explore O's border
        """
        m = len(board)
        n = len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        invalid_O = set()

        def find_invalid(invalid_O: set[tuple[int]], board: list[list[str]]):
            q = []
            for i in range(0, m):
                if i == 0 or i == m-1:
                    j_step = 1
                else:
                    j_step = n-1
                for j in range(0, n, j_step):
                    if board[i][j] == 'O':
                        if not (i, j) in invalid_O:
                            invalid_O.add((i, j))
                            q.append((i, j))
                            idx = 0
                            while idx < len(q):
                                cur_i, cur_j = q[idx]
                                for ii, jj in directions:
                                    next_i, next_j = cur_i+ii, cur_j+jj
                                    if 0 <= next_i < m and 0 <= next_j < n and board[next_i][next_j] == 'O' and (next_i, next_j) not in invalid_O:
                                        q.append((next_i, next_j))
                                        invalid_O.add((next_i, next_j))
                                idx += 1
        find_invalid(invalid_O, board)
        print(invalid_O)
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O' and (i, j) not in invalid_O:
                    board[i][j] = 'X'
        print(invalid_O)

    def solveII(self, board: List[List[str]]) -> None:
        """
        DFS
        seems fine to add into invalid at both pop or append time
        and not effect run time
        creating another m*n to mark invalid or modify in-place(then change it back) will be faster
        (by avoiding set's potential hash time)
        if invalid: [i][j]  = 'I'
        then in second loop:
        if [i][j]=='I':
            [i][j]='O
        the purpose is simple: avoid changing the invalid ones
        """
        m = len(board)
        n = len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        invalid_O = set()

        def find_invalid(invalid_O: set[tuple[int]], board: list[list[str]]):
            for i in range(0, m):
                if i == 0 or i == m-1:
                    j_step = 1
                else:
                    j_step = n-1
                for j in range(0, n, j_step):
                    if board[i][j] == 'O':
                        if not (i, j) in invalid_O:
                            stk = [(i, j)]
                            invalid_O.add((i, j))  # purning

                            while stk:
                                cur_i, cur_j = stk.pop()
                                # invalid_O.add((cur_i, cur_j))
                                for ii, jj in directions:
                                    next_i, next_j = cur_i+ii, cur_j+jj
                                    if 0 <= next_i < m and 0 <= next_j < n and board[next_i][next_j] == 'O' and (next_i, next_j) not in invalid_O:
                                        stk.append((next_i, next_j))
                                        invalid_O.add((next_i, next_j))

        find_invalid(invalid_O, board)
        print(invalid_O)
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O' and (i, j) not in invalid_O:
                    board[i][j] = 'X'


t = [['O']]
t = [['X']]
t = [['X', 'X', 'X'], ['X', 'O', 'X'], ['X', 'X', 'X']]
t = [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'X', 'X']]
r = Solution().solveII(t)
# r = Solution().solve(t)
print(t)
