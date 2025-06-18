import copy


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        '''
        mark gird as used in each attempt(different attenpt should not interupt each other)
        a path parent dict (key: tuple of current idx, value: tuple of prev idx)
        test is relatively small
        '''
        find = False
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        # O(N*M)
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    stack = []
                    path = {(i, j): None}
                    char_idx = 0
                    stack.append((i, j, char_idx, path))
                    while stack and (not find):
                        # start: tuple
                        cur_i, cur_j, char_idx, path = stack.pop()
                        if char_idx == len(word)-1:
                            find = True
                            break
                        for d in directions:
                            next_i, next_j = cur_i+d[0], cur_j+d[1]
                            if (-1 < next_i < m) and (-1 < next_j < n) and ((next_i, next_j)not in path) and (board[next_i][next_j] == word[char_idx+1]):
                                new_path = copy.copy(path)
                                new_path[(next_i, next_j)] = (i, j)
                                stack.append((next_i, next_j, char_idx+1, new_path))
                            # if no next word: break
                            # if multiple(up to 3) choice:

        return find


t = (['A'], 'A')
t = (['A'], 'B')
# t = ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCCED')
# t = ([["A", "B", "C", "C"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCCED')
r = Solution().exist(t[0], t[1])

print(r)
