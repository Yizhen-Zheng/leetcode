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
        '''
        MOD = 1000000007

        def rec(node, height, remain):
            if height > m:
                return 0

            if node == n:
                return 2 if remain else 1

            return (2 if remain else 1) * rec(node+1, height+1, True)+(rec(node+1, height, False) if remain else 0)
        r = rec(1, 1, False)
        return r


# t = (1, 3)
# t = (3, 3)
# t = (3, 2)
t = (4, 3)
r = Solution().findBTWithNNodesMHeightI(t[0], t[1])
print(r)
