from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        '''
        review
        7:58-8:13
        15min
        i remember this should be able to do with DFS?
        '''
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        step = 0
        count_fresh = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    count_fresh += 1
        while q:
            cur_len = len(q)
            for _ in range(cur_len):
                cur_i, cur_j = q.popleft()
                for ii, jj in directions:
                    newi, newj = cur_i+ii, cur_j+jj
                    if -1 < newi < m and -1 < newj < n and grid[newi][newj] == 1:
                        count_fresh -= 1
                        grid[newi][newj] = 2  # rotten next
                        q.append((newi, newj))
            step += 1 if q else 0
        return step if count_fresh == 0 else -1


t = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
r = Solution().orangesRotting(t)
print(r)
