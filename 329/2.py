from collections import deque


class Solution:
    def longestIncreasingPathI(self, matrix: list[list[int]]) -> int:
        '''
        at least 1
        time complexity: O(m*n)
        space complexity: O(m*n)
        queue version (failed to implement myself)
        '''
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        maximum = 0
        for i in range(m):
            for j in range(n):
                for dx, dy in directions:
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] < matrix[i][j]:
                        dp[i][j] += 1
        # above: mark every number's 'smaller neighbors''s number
        [print(l)for l in dp]
        # push all local smallest into quque
        queue = deque([(x, y)for x in range(m) for y in range(n) if dp[x][y] == 0])
        print(queue)
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                # pop start point
                for dx, dy in directions:
                    # explore greater neighbor
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                        dp[ni][nj] -= 1
                        if dp[ni][nj] == 0:
                            queue.append((ni, nj))
            maximum += 1
        return maximum

    def longestIncreasingPathII(self, matrix: list[list[int]]) -> int:
        '''
        at least 1
        time complexity: O(m*n)
        space complexity: O(m*n)
        stack version (failed to implement myself)
        '''
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0]*n for _ in range(m)]

        def dfs(init_i, init_j):
            # stack based dfs
            if dp[init_i][init_j]:
                return dp[init_i][init_j]
            stack = [(init_i, init_j, 0, 1)]
            path = []
            while stack:
                print('s:', stack)
                print('p:', path)
                i, j, state, current_max = stack.pop()
                if dp[i][j]:
                    if path:
                        parent_i, parent_j, parent_max = path[-1]
                        new_max = max(parent_max, 1+dp[i][j])
                        path[-1] = (parent_i, parent_j, new_max)
                    continue
                if state == 0:
                    # if it's new visited(explore)
                    path.append((i, j, current_max))
                    stack.append((i, j, 1, current_max))
                    # traceback
                    for dx, dy in directions:
                        # explore greater neighbor
                        ni, nj = i+dx, j+dy
                        if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j] and not dp[ni][nj]:
                            stack.append((ni, nj, 0, 1))
                else:
                    # trace back
                    maximum = current_max
                    for di, dj in directions:
                        ni, nj = i+di, j+dj
                        if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j] and dp[ni][nj]:
                            maximum = max(maximum, 1+dp[ni][nj])
                    dp[i][j] = maximum
                    path.pop()

                    if path:
                        parent_i, parent_j, parent_max = path[-1]
                        new_max = max(parent_max, 1 + maximum)
                        path[-1] = (parent_i, parent_j, new_max)
            return dp[init_i][init_j]

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))

        [print(l) for l in dp]
        return res

    def longestIncreasingPathIII(self, matrix: list[list[int]]) -> int:
        '''
        at least 1
        time complexity: O(m*n)
        space complexity: O(m*n)
        stack version (failed to implement myself)
        '''
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0]*n for _ in range(m)]

        def compute(init_i, init_j):
            # stack based dfs
            if dp[init_i][init_j]:
                return dp[init_i][init_j]
            # post order traversal

            def dfs(i, j):
                # for current entry, remaining un-computed nodes to form the optimized path
                local_stack = [(i, j)]
                nodes_in_path = []
                local_visited = set()
                while local_stack:
                    ci, cj = local_stack.pop()
                    if (ci, cj) in local_visited or dp[ci][cj]:
                        continue
                    local_visited.add((ci, cj))
                    nodes_in_path.append((ci, cj))
                    for di, dj in directions:
                        ni, nj = ci+di, cj+dj
                        if 0 <= ni < m and 0 <= nj < n and (matrix[ni][nj] > matrix[ci][cj]) and (not dp[ni][nj]) and ((ni, nj) not in local_visited):
                            local_stack.append((ni, nj))
                return nodes_in_path

            node_to_compute = dfs(init_i, init_j)
            node_to_compute.sort(key=lambda x: matrix[x[0]][x[1]], reverse=True)
            # this ensures we alway start from either greatest node(returns 1) or can retrive value from dp
            for i, j in node_to_compute:
                if dp[i][j]:
                    continue
                max_path = 1
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and (matrix[ni][nj] > matrix[i][j]) and (dp[ni][nj]):
                        # add biggest neighbor's value
                        max_path = max(max_path, 1+dp[ni][nj])
                dp[i][j] = max_path

            return dp[init_i][init_j]

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, compute(i, j))

        [print(l) for l in dp]
        return res


t = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
# t = [[1]]
# t = [[1, 9, 5]]
# r = Solution().longestIncreasingPathI(t)
# r = Solution().longestIncreasingPathII(t)
r = Solution().longestIncreasingPathIII(t)
print(r)
