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
        n: total nodes number
        m: maximum tree height 
        total possible ways = left posible way * right posible ways , a product, not add
        if have 3(n) nodes to assign, there are n+1 ways:
            left 0, right 3 -> rec(0, height-1)*rec(3, height-1)
            left 1, right 2 -> rec(1, height-1)*rec(2, height-1)
            left 2, right 1 -> rec(2, height-1)*rec(1, height-1)
            left 3, right 0 -> rec(3, height-1)*rec(0, height-1)
        therefore total answer in this layer(height) should be a sum of 4 ways
        '''
        MOD = 1000000007

        def rec(node_number, height):
            if node_number == 0:  # 0 nodes has one way to assign(empty)
                return 1

            if height == 0:  # not sufficient height means current branch is invalid
                return 0

            res = 0
            # left_node_number won't reach node_number, cuz current tree(parent) takes one from node_number
            for left_node_number in range(node_number):
                res += rec(left_node_number, height-1) * rec(node_number-left_node_number-1, height-1) % MOD
                res = res % MOD
            return res
        r = rec(n, m)
        return r

    def findBTWithNNodesMHeightII(self, n: int, m: int) -> int:
        '''
        with memorization
        dp is a table with 2 variable to record all the possible combinatinos, not limited to graph or so on 
        it can hold any types of 2 var, like this case hight and node number => possible ways 
        '''
        MOD = 1000000007
        dp = [[1]+([0]*(n)) for _ in range(m+1)]
        # print('\n'.join(map(str, dp)))

        def rec(node_number, height):
            if dp[height][node_number]:
                return dp[height][node_number]

            if height == 0:  # not sufficient height means current branch is invalid
                return 0
            if node_number == 0:  # 0 nodes has one way to assign(empty)
                dp[height][node_number] = 1
                return 1

            res = 0
            # left_node_number won't reach node_number, cuz current tree(parent) takes one from node_number
            for left_node_number in range(node_number):
                res += rec(left_node_number, height-1) * rec(node_number-left_node_number-1, height-1) % MOD
                res = res % MOD
            dp[height][node_number] = res
            return res
        r = rec(n, m)
        # print('\n'.join(map(str, dp)))
        return r

    def findBTWithNNodesMHeightIII(self, n: int, m: int) -> int:
        MOD = 1000000007
        dp = [[0]*(n+1) for _ in range(m+1)]
        [print(l) for l in dp]

        def rec(nodes, max_height):
            if nodes == 0:
                dp[max_height][nodes] = 1
                return 1
            if max_height == 0:
                return 0
            res = 0
            for left_node_number in range(nodes):
                res = (res+rec(left_node_number, max_height-1)*rec(nodes-1-left_node_number, max_height-1) % MOD) % MOD
            dp[max_height][nodes] = res
            return res

        r = rec(n, m)
        print('\n'.join(map(str, dp)))

        return r


t = (1, 3)
# t = (3, 3)
# t = (3, 2)
t = (4, 3)
# r = Solution().findBTWithNNodesMHeightI(t[0], t[1])
# r = Solution().findBTWithNNodesMHeightII(t[0], t[1])
r = Solution().findBTWithNNodesMHeightIII(t[0], t[1])
print(r)
