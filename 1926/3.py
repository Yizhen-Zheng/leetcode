class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        '''
        not work
        Try to improve run time
        '''
        m = len(maze)
        n = len(maze[0])
        res = [[float('inf') for _ in range(n)] for _ in range(m)]
        queue = [(entrance[0], entrance[1], 0)]
        idx = 0
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def walk(i: int, j: int, distance: int):
            res[i][j] = min(distance, res[i][j])
            maze[i][j] = '+'
            for direction_i, direction_j in directions:
                new_i, new_j = i+direction_i, j+direction_j
                if 0 <= new_i < m and 0 <= new_j < n and maze[new_i][new_j] == '.':
                    queue.append((new_i, new_j, distance+1))

        while idx < len(queue):
            i, j, d = queue[idx]
            walk(i, j, d)
            idx += 1

        print(maze)
        print(res)
        res[entrance[0]][entrance[1]] = float('inf')
        distance = float('inf')
        for i in range(m):
            for j in range(n):
                if (i > 0 and i < m-1) and (j > 0 and j < n-1):
                    continue
                distance = min(res[i][j], distance)
                print(distance)
        return distance if distance > 0 and distance != float('inf') else -1


t1 = ([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2])
t2 = ([[".", "+"]], [0, 0])
t3 = ([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0])

# r = Solution().nearestExit(t1[0], t1[1])
# r = Solution().nearestExit(t2[0], t2[1])
r = Solution().nearestExit(t3[0], t3[1])

print(r)
