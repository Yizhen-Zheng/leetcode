import math


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        '''
        '''
        max_p = 0
        buy = math.inf
        for price in prices:
            max_p = max(max_p, price-buy)
            buy = min(buy, price)
        return max_p


t = [7, 1, 5, 3, 6, 4]
r = Solution().maxProfit(t)
print(r)
