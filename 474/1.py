class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        '''
        m 0, n 1
        2 constrains for the pack
        2D, the biggiest size when m,n
        t = O(2^n), for i, pick or not pick
        BF
        45 min ish
        '''
        cnt = []
        for s in strs:
            zero_num = s.count('0')
            one_num = s.count('1')
            cnt.append((zero_num, one_num))
        print(cnt)
        best_size = 0

        def pick(idx: int, m: int, n: int, size: int):
            nonlocal best_size
            if m < 0 or n < 0:
                return
            best_size = max(best_size, size)
            if idx >= len(strs):
                return
            # not pick cur:
            pick(idx+1, m, n, size)
            # pick cur:
            z_cost, o_cost = cnt[idx]
            newz, newo = m-z_cost, n-o_cost
            if not (newz < 0 or newo < 0):
                best_size = max(best_size, size+1)
                pick(idx+1, m-z_cost, n-o_cost, size+1)
        pick(0, m, n, 0)
        return best_size

    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        '''
        try dp
        top down dp
        how to make sure we're not using the same elems again?
        t: O(n**3)
        s: O(n**3)
        '''
        dp: dict[tuple[int, int, int], int] = {}  # need access 0 ones/zeros to m/n ones/zeros, not stop at m/n-1
        # idx, m, n
        # remain(when non space is used, subset size is 0(not pick at all))
        cnt = []  # convert str to m,n cost
        for s in strs:
            zero_num = s.count('0')
            one_num = s.count('1')
            cnt.append((zero_num, one_num))
        length = len(strs)

        def pick(idx: int, m: int, n: int):
            if (idx, m, n) in dp:
                return dp[(idx, m, n)]
            if idx >= length:
                return 0
            z_cost, o_cost = cnt[idx]
            newz, newo = m-z_cost, n-o_cost
            pick_cur = 0
            if not (newz < 0 or newo < 0):
                pick_cur = 1+pick(idx+1, newz, newo)
            not_pick_cur = pick(idx+1, m, n)
            dp[(idx, m, n)] = max(pick_cur, not_pick_cur)
            return dp[(idx, m, n)]

        size = pick(0, m, n)
        return size

    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        '''
        solution, bottom up
        t: O(n**3)
        s: O(n**2)
        for each cell, 
            if not pick, dp[i][j] remains unchanged
            if pick, dp[i][j] is previous state's size + 1
        then UPDATE dp so it becomes the maximum state overall
        for each str, choose pickup / not, then update for ALL fessible solutions
        (by finding remaining space m>curM and n>curN)
        dp[0][0] means none of spaces is taken up, so size is 0
        dp[i][j] means so far, the maximum size can be achieved by using such many(i,j) spaces 
        the reason fill from m to zcost-1 if to avoid using same elem twice
        e.g. t=['1','0',] m=1 n=1
        dp=[[0,0],
            [0,0]]
        s='1',i in (0, 2)
            j in (1, 2):
                dp[0][0]=0(unchanged)
                dp[0][1]=1
                dp[1][0]=0
                dp[1][1]=1
        s='0',i in (1, 2)
                j in (0, 2):
                    dp[0][0]=0(unchanged)
                    dp[0][1]=0(unchanged)
                    dp[1][0]=1 <- potentially happen to be used further
                    dp[1][1]=2
        alternatively:
        tempDp=dp
        for i in range(zCost, m+1):
            for j in range(oCost, n+1):
                tempDp=max(dp[i][j], i+dp[i-zCost],[j-oCost])
        dp=tempDp
        '''
        dp = [[0]*(n+1) for _ in range(m+1)]
        for s in strs:
            zcost = s.count('0')
            ocost = s.count('1')
            for i in range(m, zcost-1, -1):
                for j in range(n, ocost-1, -1):
                    dp[i][j] = max(dp[i][j], 1+dp[i-zcost][j-ocost])
        return dp[m][n]


# t = ["10", "0001", "111001", "1", "0"]
# r = Solution().findMaxForm(t, 5, 3)
t = ["10", "0"]
r = Solution().findMaxForm(t, 2, 1)
# t = ["101000000", "1100001010", "11101000", "011010110", "0010001", "0011", "0111101111"]
# r = Solution().findMaxForm(t, 10, 11)
print(r)
