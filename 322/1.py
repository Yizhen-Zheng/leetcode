from collections import deque


class Solution:
    def coinChangeI(self, coins: list[int], amount: int) -> int:
        '''
        21:14-21:24
        looks like dp
        coins len: [1,12], coins[i]: positive, amount: 0+
        brute force: dfs
        t: O(2^n)
        s: O(n)
        '''
        coins.sort(reverse=True)

        def dfs(goal: int, path_len: list):
            if goal == 0:
                return path_len
            if goal < 0:
                return float('inf')
            min_len = float('inf')
            for coin in coins:
                new_len = dfs(goal-coin, path_len+1)
                min_len = min(new_len, min_len)
            return min_len
        res = dfs(amount, 0)
        return -1 if res == float('inf') else res

    def coinChange(self, coins: list[int], amount: int) -> int:
        '''
        at most need amount coins
        dp: idx: goal val: shortest path
        naturally choose big coin first? seems not work
        how to make the 1D dp? maybe need backtrack

        MAYBE NEED BFS(shortest path?)
        but also a bit like 1D dp, update dp[i]=min(dp[i],cur)
        yesterday - 10:44
        works!
        t: O(n*m)(if coin=[1])(amount=n)(from 0 - amount, every cur_amount needs loop all coins)
        s: O(n)
        '''
        table = [float('inf')]*amount
        # amount=0, no need for any coin
        q = deque([(0, 0)])  # cur ammount, coin number
        while q:
            cur_amount, coin_count = q.popleft()
            if cur_amount == amount:
                return coin_count
            # find smaller,update
            if cur_amount < amount and table[cur_amount] > coin_count:
                table[cur_amount] = coin_count
                for coin in coins:
                    q.append((cur_amount+coin, coin_count+1))

        return -1

    def coinChangeSolution(self, coins: list[int], amount: int) -> int:
        '''
        solution:
        bfs, iterative instead of q
        '''
        table = [float('inf')]*(amount+1)
        table[0] = 0
        for i in range(0, amount+1):
            for coin in coins:
                next_amount = i+coin
                if next_amount <= amount:
                    table[next_amount] = min(table[next_amount], table[i]+1)
        return table[-1] if table[-1] != float('inf')else -1

    def coinChangeIterativeEarlyReturn(self, coins: list[int], amount: int) -> int:
        '''
        solution:
        bfs, iterative instead of q
        why early pruning not work?
        seems if it hits a not optimal solution and adding to amount, 
        that will cause return early, cannot wait to getting the correct spot
        '''
        table = [float('inf')]*amount
        table[0] = 0
        for i in range(0, amount):
            if table[i] != float('inf'):
                for coin in coins:
                    next_amount = i+coin
                    if next_amount == amount:
                        return table[i]+1  # early pruning seems not work
                    if next_amount < amount:
                        table[next_amount] = min(table[next_amount], table[i]+1)
        return -1

    def coinChange(self, coins: list[int], amount: int) -> int:
        '''
        dp memorization(dfs)
        t: O(n*m)
        s: O(n)(stack depth + table)
        the dfs solution demostrated the recursion automatically handle the backtrack
        (all status stored in the scope, accessable once returns back)
        '''
        memo = {0: 0}

        def rec(remain: int):
            if remain in memo:  # out of range
                return memo[remain]
            if remain == 0:
                return 0
            if remain < 0:
                return float('inf')
            res = float('inf')
            for c in coins:
                res = min(res, rec(remain-c)+1)
            memo[remain] = res
            return res
        rec(amount)
        return memo[amount] if memo[amount] != float('inf') else -1

    def coinChange(self, coins: list[int], amount: int) -> int:
        '''
        the unnecessary 2D dp
        a more significantly dfs
        it will go to the deepest on one branch(like 1,1,1,1,1.. )if possible
        then try another neighbor branch from second deepest node
        t: O(n*m)
        s: O(n*m)(stack depth + table)
        '''
        memo = {}

        def rec(cur_idx: int, amount: int):
            if amount == 0:
                return 0
            if cur_idx == len(coins) or amount < 0:
                return float('inf')
            if (cur_idx, amount) in memo:
                return memo[(cur_idx, amount)]

            take_cur = 1+rec(cur_idx, amount-coins[cur_idx])
            skip_cur = rec(cur_idx+1, amount)
            memo[(cur_idx, amount)] = min(take_cur, skip_cur)
            return memo[(cur_idx, amount)]
        res = rec(0, amount)
        return res if res != float('inf') else -1


t = ([1, 2, 5], 11)
t = ([456, 117, 5, 145], 1459)
# t = ([2], 3)
r = Solution().coinChange(t[0], t[1])
print(r)
