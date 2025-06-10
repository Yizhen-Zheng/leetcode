class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        '''
        push walking to a list (queue)
        mark current minimum if it's boundary
        mark visited?
        either go down or go right
        Memorization, a grid's minimum is it's min(its upper or its left heighbour)
        N*M
        optimization to remove if i, j >0 from recursion:
        use 2 for look to fill the top-most and left-most, then use nested for loop to fill the dp, then return dp[-1][-1]
        (batch handle edges)
        '''
        m, n = len(grid), len(grid[0])
        dp = [[None] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        def findWay(i, j):
            if dp[i][j] != None:
                return dp[i][j]

            left = up = float('inf')
            if j > 0:
                left = findWay(i, j-1)
            if i > 0:
                up = findWay(i-1, j)
            dp[i][j] = grid[i][j]+min(left, up)
            return dp[i][j]

        res = findWay(m-1, n-1)
        print(dp)

        return res


# t = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
# t = [[1, 2, 3], [4, 5, 6]]
# t = [[1, 0], [5, 6]]
t = [[1, 3, 4], [6, 2, 0]]
r = Solution().minPathSum(t)

print(r)
