'''
小强现在有n个节点,他想请你帮他计算出有多少种不同的二叉树满足节点个数为n且树的高度不超过m的方案.因为答案很大,所以答案需要模上1e9+7后输出.
树的高度: 定义为所有叶子到根路径上节点个数的最大值.
例如: 当n=3,m=3时,有如下5种方案:
1 <= n, m <= 50
input: 
'''


class Solution:
    def findBTWithNNodesMHeightI(self, n: int, m: int) -> int:
        '''
        bottom-ip
        '''
        MOD = 1000000007
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if j == 0:
                    dp[i][j] = 1
                    continue
                if i == 0:
                    # if no height left, current approach won't form valid tree
                    dp[i][j] = 0
                    continue
                res = 0
                for left_node_number in range(j):
                    res = (res+(dp[i-1][left_node_number]*dp[i-1][j-left_node_number-1]) % MOD) % MOD
                dp[i][j] = res
        [print(l) for l in dp]
        return dp[m][n]

    def findBTWithNNodesMHeightII(self, n: int, m: int) -> int:
        MOD = 1000000007
        dp = [[0]*(n+1) for _ in range(2)]

        for i in range(m+1):
            for j in range(n+1):
                if j == 0:
                    dp[i % 2][j] = 1
                    continue
                if i == 0:
                    # if no height left, current approach won't form valid tree
                    dp[i % 2][j] = 0
                    continue
                res = 0
                for left_node_number in range(j):
                    res = (res+(dp[(i-1) % 2][left_node_number]*dp[(i-1) % 2][j-left_node_number-1]) % MOD) % MOD
                dp[i % 2][j] = res
            [print(l) for l in dp]
            print('')
        return dp[m % 2][n]

    def findBTWithNNodesMHeightIII(self, n: int, m: int) -> int:
        MOD = 1000000007
        dp = [0]*(n+1)
        for i in range(m+1):
            for j in range(n, -1, -1):
                if j == 0:
                    dp[j] = 1
                    continue
                if i == 0:
                    # if no height left, current approach won't form valid tree
                    dp[j] = 0
                    continue
                res = 0
                for left_node_number in range(j):
                    res = (res+(dp[left_node_number]*dp[j-left_node_number-1]) % MOD) % MOD
                dp[j] = res
            print(dp)
            print('')
        return dp[n]


t = (1, 3)
t = (3, 3)
# t = (3, 2)
t = (4, 3)
# r = Solution().findBTWithNNodesMHeightI(t[0], t[1])
# r = Solution().findBTWithNNodesMHeightII(t[0], t[1])
r = Solution().findBTWithNNodesMHeightIII(t[0], t[1])
print(r)
