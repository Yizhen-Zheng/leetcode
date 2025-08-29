from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        '''
        11:21-11:48
        27min
        if is island: 4 directions are water/out range
        note it's str '0' '1'
        denote garbage
        count groups that can be 'rotted'
        t: O(n*m)
        s: O(n*m)
        '''
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = '#'
            while q:
                x, y = q.popleft()
                for xx, yy in directions:
                    nx, ny = x+xx, y+yy
                    if -1 < nx < m and -1 < ny < n and grid[nx][ny] == '1':
                        grid[nx][ny] = '#'
                        q.append((nx, ny))
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    bfs(row, col)
                    count += 1
        return count

    def numIslands(self, grid: list[list[str]]) -> int:
        '''
        dfs:
        same as above
        t: O(n*m)
        s: O(n*m)
        '''
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0

        def dfs(x, y):
            grid[x][y] = '#'
            for xx, yy in directions:
                nx, ny = x+xx, y+yy
                if -1 < nx < m and -1 < ny < n and grid[nx][ny] == '1':
                    dfs(nx, ny)
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    dfs(row, col)
                    count += 1
        return count

    def numIslands(self, grid: list[list[str]]) -> int:
        '''
        Union find:
        '''
        m, n = len(grid), len(grid[0])
        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count_one = sum(grid[r][c] == '1' for c in range(n) for r in range(m))
        parent = [i for i in range(m*n)]

        def union(x, y):
            nonlocal count_one

            xp, yp = find(x), find(y)
            if xp != yp:  # merge
                parent[xp] = yp
                count_one -= 1
            return

        def find(idx):
            nonlocal count_one

            p = parent[idx]
            if p != idx:
                p = find(parent[idx])
            return p

        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':  # only unionfind if it's '1'
                    idx = row*m+col
                    if col < n-1 and grid[row][col+1] == '1':
                        # visit right adj ceil
                        union(idx, idx+1)
                    if row < m-1 and grid[row+1][col] == '1':
                        union(idx, idx+m)

        return count_one

    def numIslands(self, grid: list[list[str]]) -> int:
        '''
        2d union
        initially all ones are considered island
        then try to merge with others and decrease island count
        because we're traversing from top left to bottom right, 
        we can ensure previous ones are merged
        '''
        m, n = len(grid), len(grid[0])
        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count_one = 0
        parent = {}

        def union(x, y):
            nonlocal count_one
            xp, yp = find(x), find(y)
            if xp != yp:  # merge
                parent[xp] = yp
                count_one -= 1  # only mark as new found if x y don't come from same chunk
            return

        def find(idx):
            if parent[idx] != idx:  # parent is not itself
                # assign root parent
                parent[idx] = find(parent[idx])
            return parent[idx]

        #  prepare count ones and parent
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    parent[(row, col)] = (row, col)
                    count_one += 1

        for row, col in parent.keys():
            if (row, col+1) in parent:
                # visit right adj ceil
                union((row, col), (row, col+1))
            if (row+1, col) in parent:
                union((row, col), (row+1, col))

        return count_one


t = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
t = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "1"]]
# t = [['1']]
# t = [['0']]
r = Solution().numIslands(t)
print(r)
