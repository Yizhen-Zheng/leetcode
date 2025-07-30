from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        '''
        graph traverse
        BFS
        brute force: 
            every traverse mark new rotten, count how many time traversed
            until get end or find spaces
            problem: how to know when is it rotten?
            by add numbers
            if it's a rotten one, takes 0, and its neighbor is one
            and keep recording the maximum in dp
        traverse: find rotten, then mark expanding
        17min + 10min(to complete code) + 9min(debug)
        if no oranges, return 0(takes no time to rot)
        '''
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m = len(grid)
        n = len(grid[0])
        count = [[float('inf')]*n for _ in range(m)]
        max_time = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q = deque([(i, j)])
                    count[i][j] = 0  # takes 0 min to rottent if already rotten
                    while q:
                        cur_i, cur_j = q.popleft()
                        cur_time = count[cur_i][cur_j]
                        # expand
                        for ii, jj in directions:
                            next_i, next_j = cur_i+ii, cur_j+jj
                            if -1 < next_i < m and -1 < next_j < n:
                                # check can expand
                                if grid[next_i][next_j] == 1 and count[next_i][next_j] > cur_time+1:
                                    # only expand fresh ones or can be faster
                                    # if grid[next_i][next_j] == 1:
                                    count[next_i][next_j] = min(count[next_i][next_j], cur_time+1)
                                    q.append((next_i, next_j))
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:  # only check fresh or rotten, skip empty
                    if count[i][j] == float('inf'):
                        return -1
                    else:
                        max_time = max(max_time, count[i][j])
        return max_time

    def orangesRotting(self, grid: list[list[int]]) -> int:
        '''
        graph traverse
        BFS(globally traverse), more efficient
        all rotten origin spots -> all fresh that distance one from rotten -> ...
        more efficient with a natual duplication prevention
        pre calculate freshes and entry points
        instead comparing max, mark all rotten ones as 2
        so using a global q, this proves closer freshes are visited first
        and prevents adding rotten freshes back to queue
        20min
        '''
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m = len(grid)
        n = len(grid[0])
        count_time = 0
        remain = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    remain += 1
        while q:  # natrually exit if no freshes can be added
            # scann current layer
            for _ in range(len(q)):
                cur_i, cur_j = q.popleft()
                # expand spot
                for ii, jj in directions:
                    next_i, next_j = cur_i+ii, cur_j+jj
                    if -1 < next_i < m and -1 < next_j < n:
                        # check can expand
                        if grid[next_i][next_j] == 1:
                            grid[next_i][next_j] = 2  # mark as rotten
                            q.append((next_i, next_j))
                            remain -= 1
            count_time += 1
        return max(0, count_time-1) if remain == 0 else -1


t = [[0, 2]]
t = [[0, 0]]
t = [[0, 2], [1, 0]]
# t = [[0, 2], [0, 1]]
# t = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
r = Solution().orangesRotting(t)
print(r)
