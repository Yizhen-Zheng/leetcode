class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        '''
        push walking to a list (queue)
        mark current minimum if it's boundary
        mark visited?
        either go down or go right
        Memorization, a grid's minimum is it's min(its upper or its left heighbour)
        O(N*M) * [time every cell take (this case O(1))]
        optimization to remove if i, j >0 from recursion:
        use 2 for look to fill the top-most and left-most, then use nested for loop to fill the dp, then return dp[-1][-1]
        (batch handle edges)
        space efficient way:
        keep a list of previous row, and prev cell ([i][j-1])
        '''
        m, n = len(grid), len(grid[0])
        dp = [None] * n
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j-1]+grid[0][j]

        for i in range(1, m):
            dp[0] = dp[0]+grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1])+grid[i][j]
        return dp[-1]


t = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
# t = [[1, 2, 3], [4, 5, 6]]
# t = [[1, 0], [5, 6]]
# t = [[1, 3, 4], [6, 2, 0]]
r = Solution().minPathSum(t)

print(r)
