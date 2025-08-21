from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        '''
        at least one 0
        14:45-14:56
        14:56-16:02
        this dfs not work 
        bfs,
        dfs
        '''
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(mat)
        n = len(mat[0])

        ans = [[0]*n for _ in range(m)]
        todo = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    todo.append((i, j))
                    ans[i][j] = float('inf')

        def dfs(x, y, visited: set[tuple[int, int]]):
            if mat[x][y] == 0:
                return 0
            if ans[x][y] != float('inf'):
                return ans[x][y]
            min_dist = float('inf')
            for xx, yy in directions:
                new_x, new_y = x+xx, y+yy
                if -1 < new_x < m and -1 < new_y < n and (new_x, new_y)not in visited:
                    visited.add((new_x, new_y))
                    min_dist = min(min_dist, dfs(new_x, new_y, visited)+1)
            ans[x][y] = min_dist
            return min_dist
        for x, y in todo:
            visited = {(x, y)}
            dfs(x, y, visited)

        return ans

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        '''
        at least one 0
        16:02-16:24
        bfs
        t: O(n*m)
        s: O(n*m)
        '''
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(mat)
        n = len(mat[0])
        ans = [[float('inf')]*n for _ in range(m)]
        q = deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    ans[i][j] = 0

        while q:
            x, y, dist = q.popleft()
            ans[x][y] = min(ans[x][y], dist)
            for xx, yy in directions:
                new_x, new_y = x+xx, y+yy
                if -1 < new_x < m and -1 < new_y < n and ans[new_x][new_y] == float('inf'):
                    q.append((new_x, new_y, dist+1))

        return ans

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        '''
        at least one 0
        16:02-16:24
        bfs
        t: O(n*m)
        s: O(n*m)
        why it's important to mark 'visited' before pushing to queue, instead of after poping:
        for one cell, it may be able to reached from many origins,
        the ones come after(be popped later) may have larger value, cause overwrite with wrong answer
        so either use min when update at poping, or early pruning
        '''
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(mat)
        n = len(mat[0])
        ans = [[float('inf')]*n for _ in range(m)]
        q = deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    ans[i][j] = 0
        # iterative expand
        while q:
            x, y = q.popleft()
            for xx, yy in directions:
                new_x, new_y = x+xx, y+yy
                if -1 < new_x < m and -1 < new_y < n and ans[new_x][new_y] == float('inf'):
                    ans[new_x][new_y] = ans[x][y]+1
                    q.append((new_x, new_y))
        return ans


# t = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
t = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
# t = [[0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 1, 0], [1, 0, 1, 1, 1], [1, 0, 0, 0, 1]]


r = Solution().updateMatrix(t)
print(r)
