class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        '''
        2-ptr
        b-f: t:O(n^2)
        10:14 - 10:27,13min
        -10:34 - 11:02, 28min
        total 41 min
        divide and conquer(for every pos, the order if left part doesn'y matter)
        divide and conquer:
        t: O(nlogn)?
        s:O(logn)(stack depth)
        # l, r = 0, n-1
        # while l < r:
        #     best = max(best, prices[r]-prices[l])
        #     if prices[r-1] > prices[r]:
        #         r -= 1
        #     # elif prices[l+1] < prices[l]:
        #     #     l += 1
        #     else:
        #         l += 1
        '''
        n = len(prices)
        best = 0

        def rec(l, r):
            if l == r:
                return prices[l], prices[l], 0
            m = l+(r-l)//2
            min_l_a, max_r_a, a = rec(l, m)
            min_l_b, max_r_b, b = rec(m+1, r)
            return (min(min_l_a, min_l_b), max(max_r_a, max_r_b), max(a, b, max_r_b-min_l_a))
        _, _, best = rec(0, n-1)
        return best

    def maxProfit(self, prices: list[int]) -> int:
        '''
        kadane 
        t: O(n)
        s: O(1)
        pick or refresh
        '''
        n = len(prices)
        cur, best = 0, 0  # cur: b and s at day 1
        for i in range(1, n):
            expand = cur-prices[i-1]+prices[i]  # undo prev sell, sell today
            restart = 0  # buy today
            cur = max(expand, restart)  # calculate gain
            best = max(best, cur)
        return best

    def maxProfit(self, prices: list[int]) -> int:
        '''
        2 ptr, i: cur price, buy: when to buy
        if cur price > buy price, compare profit if sell at cur
        else, means we found better buy price, update
        '''
        n = len(prices)
        buy, best_profit = 0, 0
        # buy: idx, at 1st day
        for i in range(n):
            best_profit = max(best_profit, prices[i]-prices[buy])  # assume i is sell point
            if prices[i] < prices[buy]:  # if it's better buy point, update
                buy = i
        return best_profit


t = [1, 2, 3]
# t = [3, 1]
# t = [3, 1]
r = Solution().maxProfit(t)
print(r)
