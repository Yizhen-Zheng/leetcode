class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        '''
        use the matrix given, make mark (fill each grids the is '.') 
        need condition to recognize if current grid is exit
        for every step, we mark the last gird as 'visited'
        we can use the origin list to mark, since the paths are not interrupting each other
        current_step = prev_step + 1
        DFS will encounter a circle which will miss the smallest path bcz we've marked that as a '+', so we won't get there
        '''
        m = len(maze)
        n = len(maze[0])
        res = [[float('inf') for _ in range(n)] for _ in range(m)]

        def walk(current_direction: list[int], prev_step: int, prev_idx: list):
            '''go to next, and mark current as visited'''
            i, j = current_direction
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            # if maze[i][j] != '.':
            if maze[i][j] == '+':
                return

            res[i][j] = min(res[i][j], prev_step+1)
            maze[i][j] = '!'

            count = 0
            for next_i in range(-1, 2):
                for next_j in range(-1, 2):
                    count += 1
                    if count % 2 == 1:
                        '''prevent [-1,1],[0,0]'''
                        continue
                    elif next_i == prev_idx[0] and next_j == prev_idx[1]:
                        continue
                    else:
                        walk([i+next_i, j+next_j], res[i][j], [i, j])

            # walk([i-1, j], res[i][j], [i, j])
            # walk([i, j-1], res[i][j], [i, j])
            # walk([i+1, j], res[i][j], [i, j])
            # walk([i, j+1], res[i][j], [i, j])

        walk(entrance, -1, [None, None])
        print(maze)

        print(res)
        res[entrance[0]][entrance[1]] = float('inf')
        distance = float('inf')
        for i in range(m):
            for j in range(n):
                if (i > 0 and i < m-1) and (j > 0 and j < n-1):
                    continue
                distance = min(res[i][j], distance)
        return distance if distance > 0 and distance != float('inf') else -1


t1 = ([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2])
t2 = ([[".", "+"]], [0, 0])
t3 = ([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0])
t4 = ([["+", ".", "+", "+", "+", "+", "+"], ["+", ".", "+", ".", ".", ".", "+"], ["+", ".", "+",
      ".", "+", ".", "+"], ["+", ".", ".", ".", ".", ".", "+"], ["+", "+", "+", "+", ".", "+", "."]], [0, 1])
r = Solution().nearestExit(t1[0], t1[1])
# r = Solution().nearestExit(t2[0], t2[1])
# r = Solution().nearestExit(t3[0], t3[1])
# r = Solution().nearestExit(t4[0], t4[1])
print(r)
