class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        9:48-10:00
        seems dp
        t: O(n*m)
        s: O(n*m)
        '''
        dp = [[0]*n for _ in range(m)]
        for col in range(n):
            dp[0][col] = 1
        for row in range(m):
            dp[row][0] = 1
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row][col-1]+dp[row-1][col]

        return dp[-1][-1]

    def uniquePaths(self, m: int, n: int) -> int:
        '''
        10:00-10:08
        try space optimization
        t: O(n*m)
        s: O(n)

        '''
        if m == 1 or n == 1:
            return 1
        dp = [1]*n
        for _ in range(1, m):
            for col in range(1, n):
                dp[col] = dp[col-1]+dp[col]
        return dp[-1]

    def uniquePaths(self, m: int, n: int) -> int:
        '''
        brute force:
        '''
        def rec(row, col):
            if row >= m or col >= n:
                return 0
            if row == m-1 and col == n-1:
                return 1
            return rec(row+1, col) + rec(row, col+1)
        return rec(0, 0)

    def uniquePaths(self, m: int, n: int) -> int:
        '''
        memorization: top down
        first go to deepest, then turn back from base case
        '''
        dp = [[0]*n for _ in range(m)]

        def rec(row, col):
            if row >= m or col >= n:
                return 0
            if row == m-1 and col == n-1:
                return 1
            if dp[row][col]:
                return dp[row][col]
            dp[row][col] = rec(row+1, col) + rec(row, col+1)
            return dp[row][col]
        res = rec(0, 0)
        print(dp)
        return res


t = (3, 7)
r = Solution().uniquePaths(t[0], t[1])
print(r)
