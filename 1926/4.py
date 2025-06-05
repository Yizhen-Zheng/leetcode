from collections import deque


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        '''
        yield: return multiple times
        deque: double ended queue (is a doubly linked list)
        alternatively use a normal queue with idx

        if want to avoid modify original maze: 
            use a lookup
            visited = [[None]*n for _ in range(m)]...

        '''

        m = len(maze)
        n = len(maze[0])

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        # visited = [[None]*n for _ in range(m)]     <----avoid modify original maze

        def is_exit(i: int, j: int) -> bool:
            return i*j == 0 or i == m-1 or j == n-1

        def find_next(i: int, j: int):
            for direction_i, direction_j in directions:
                new_i, new_j = i+direction_i, j+direction_j
                if 0 <= new_i < m and 0 <= new_j < n and maze[new_i][new_j] != '+':
                    # if 0 <= new_i < m and 0 <= new_j < n and maze[new_i][new_j] != '+' and visited[new_i][new_j] == None:     <----avoid modify original maze
                    yield new_i, new_j

        # dq = deque([(entrance[0], entrance[1], 0)])
        q = [(entrance[0], entrance[1], 0)]
        idx = 0
        maze[entrance[0]][entrance[1]] = '+'
        # visited[entrance[0]][entrance[1]] = True     <----avoid modify original maze

        while idx < len(q):
            # i, j, d = dq.popleft()
            i, j, d = q[idx]
            for next_i, next_j in find_next(i, j):
                maze[next_i][next_j] = '+'
                # visited[next_i][next_j] = True     <----avoid modify original maze
                if is_exit(next_i, next_j):
                    return d+1
                q.append((next_i, next_j, d+1))
            idx += 1

        print(maze)
        return -1


t1 = ([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2])
t2 = ([[".", "+"]], [0, 0])
t3 = ([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0])
t4 = ([["+", ".", "+", "+", "+", "+", "+"], ["+", ".", "+", ".", ".", ".", "+"], ["+", ".", "+",
      ".", "+", ".", "+"], ["+", ".", ".", ".", ".", ".", "+"], ["+", "+", "+", "+", ".", "+", "."]], [0, 1])

# r = Solution().nearestExit(t1[0], t1[1])
# r = Solution().nearestExit(t2[0], t2[1])
# r = Solution().nearestExit(t3[0], t3[1])
r = Solution().nearestExit(t4[0], t4[1])

print(r)
