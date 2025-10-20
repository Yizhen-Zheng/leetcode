from collections import deque


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        '''
        5:34-5:52
        combination dedup
        t: O(n!*n), (maybe n is len(coins)
        s: O(n!*n)
        '''
        coins.sort()
        ans = 0
        q = deque([(0, 0)])
        n = len(coins)
        while q:
            cur_amount, idx_used = q.popleft()
            if cur_amount == amount:  # this branch is done, no need to grow leaf
                ans += 1
                continue  # go another branch
            for i in range(idx_used, n):
                if (i > idx_used) and coins[i] == coins[i-1]:
                    continue  # prune horizontally, prevent same branch
                if cur_amount + coins[i] > amount:
                    break

                q.append((cur_amount + coins[i], i))
        return ans

    def change(self, amount: int, coins: list[int]) -> int:
        '''
        BF,dfs
        '''
        coins.sort()
        n = len(coins)

        def dfs(remain_amount: int, start_idx: int):
            if remain_amount == 0:
                return 1
            sub_ans = 0
            for i in range(start_idx, n):
                if i > start_idx and coins[i] == coins[i-1]:
                    continue
                if remain_amount-coins[i] < 0:
                    break
                count = dfs(remain_amount-coins[i], i)
                sub_ans += count
            return sub_ans
        count_perm = dfs(amount, 0)
        return count_perm

    def change(self, amount: int, coins: list[int]) -> int:
        '''
        as its just count, need to use memo for TLE, is it 2D dp?
        works
        t: O(m*n)
        s: O(m*n)
        seems not sorting still works
        '''
        # coins.sort()
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n)]
        # first row
        for am in range(amount+1):
            dp[0][am] = 1 if am % coins[0] == 0 else 0

        for coin_idx in range(1, n):
            cur_coin = coins[coin_idx]
            for am in range(amount+1):
                not_use_cur = dp[coin_idx-1][am]
                if am < cur_coin:
                    dp[coin_idx][am] = not_use_cur
                    continue
                use_cur = dp[coin_idx][am-cur_coin]
                dp[coin_idx][am] = not_use_cur+use_cur
        return dp[n-1][amount]

    def change(self, amount: int, coins: list[int]) -> int:
        '''
        t: O(m*n)
        s: O(m*n)
        space opt
        '''
        n = len(coins)
        # first row
        dp = [1 if am % coins[0] == 0 else 0 for am in range(amount+1)]
        for coin_idx in range(1, n):
            cur_coin = coins[coin_idx]
            for am in range(amount+1):
                not_use_cur = dp[am]
                if am < cur_coin:
                    dp[am] = not_use_cur
                    continue
                use_cur = dp[am-cur_coin]
                dp[am] = not_use_cur+use_cur
        return dp[amount]

    def change(self, amount: int, coins: list[int]) -> int:
        '''
        t: O(m*n)
        s: O(m*n)
        pruning!
        oh! the grid can be left untougched! cuz there's only one row!
        all amount < cur coin won't change!
        '''
        n = len(coins)
        # first row
        dp = [1 if am % coins[0] == 0 else 0 for am in range(amount+1)]
        for coin in coins:
            for am in range(coin, amount+1):
                not_use_cur = dp[am]
                use_cur = dp[am-coin]
                dp[am] = not_use_cur+use_cur
        return dp[amount]


t = (5, [1, 2, 3])
# t = (3, [1, 2, 3])
r = Solution().change(t[0], t[1])
print(r)
