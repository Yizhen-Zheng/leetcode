
class Solution:

    def canPartition(self, nums: list[int]) -> bool:
        '''
        11:05-11:07,11:14-11:24
        13min, not work
        all nums positive
        sort, dp partition point
        seems require dp
        not work:
        '''
        n = len(nums)
        l_sum, r_sum = 0, sum(nums)
        nums.sort()  # O(logn)
        for i in range(n):
            l_sum += nums[i]
            r_sum -= nums[i]
            if l_sum == r_sum:
                return True
        return False

    def canPartition(self, nums: list[int]) -> bool:
        '''
        brute force: duplicated binary tree branch calculating
        t: O(n^n)
        s:O(n)
        '''
        n = len(nums)

        def rec(l_sum: int, r_sum: int, idx: int):
            if idx >= n:
                return l_sum == r_sum
            cur = nums[idx]
            # put cur in left:
            l = rec(l_sum+cur, r_sum, idx+1)
            # put cur in right:
            r = rec(l_sum, r_sum+cur, idx+1)
            return l or r
        return rec(0, 0, 0)

    def canPartition(self, nums: list[int]) -> bool:
        '''BF 2ed version'''
        n = len(nums)
        total = sum(nums)
        if total & 1:
            return False

        def rec(goal: int, idx):
            if goal == 0:
                return True
            if idx >= n or goal < 0:
                return False
            pick = rec(goal-nums[idx], idx+1)
            not_pick = rec(goal, idx+1)
            return pick or not_pick
        return rec(total//2, 0)

    def canPartition(self, nums: list[int]) -> bool:
        '''
        rec: pick or not pick
        DP[idx][sum]: can add to sum(through some picks and some throws) start from positino idx

        dp: idx * sum//2
        if 
        '''
        total = sum(nums)
        if total % 2:
            return False
        n = len(nums)
        goal = total//2
        memo = {}
        for i in range(n):
            memo[i] = {}

        def rec(goal: int, idx: int):
            if goal == 0:
                return True
            if idx >= n or goal < 0:
                return False
            if goal in memo[idx]:
                return memo[idx][goal]
            pick = rec(goal-nums[idx], idx+1)
            not_pick = rec(goal, idx+1)
            res = pick or not_pick
            memo[idx][goal] = res
            return res
        res = rec(goal, 0)
        return res

    def canPartition(self, nums: list[int]) -> bool:
        '''
        1D dp
        this seems NOT WORK,
        still need 
        table{(goal,idx)}, equal to 2D
        '''
        total = sum(nums)
        if total % 2:
            return False
        n = len(nums)
        goal = total//2
        memo = {}

        def rec(goal: int, idx: int):
            if goal == 0:
                return True
            if idx >= n or goal < 0:
                return False
            if goal in memo and memo[goal] == True:
                return memo[goal]
            # pick = rec(goal-nums[idx], idx+1)
            # not_pick = rec(goal, idx+1)
            res = rec(goal-nums[idx], idx+1) or rec(goal, idx+1)
            memo[goal] = res
            return res
        res = rec(goal, 0)

        return res

    def canPartition(self, nums: list[int]) -> bool:
        '''
        if len < 32 , bitmask if very suitable
        dp build path to reach total//2
        11:24-12:09 yeh!
        layer width: 2**N
        t: O(n*2^n)
        s: O(2^n)(number of results: up to sum//2)
        e,g, [1,1,2,2]
        num=1
            origin={0}
            build={0,1}(pick or not)
        num=1
            origin={0,1}
            build={0,1,2}
        num=2
            origin={0,1}
            build={0,1,2,3,4}, return!
        '''
        total = sum(nums)
        if total % 2:
            return False
        goal = total//2
        memo = {0}
        for num in nums:
            origin = memo.copy()
            for s in origin:
                new = num+s
                if new == goal:
                    return True
                memo.add(new)  # do nothing if elem originnally exists
                # equal to dp[cur_sum] or dp[cur_sum - picked_builder_num]
        return False

    def canPartition(self, nums: list[int]) -> bool:
        '''
        dp, we can still dp wthiout set,
        using backloop to prevent duplicate and check
        e,g, [1,1,2,2]
        init memo:
        [T,F,F,F]
            num=1,[T,T,F,F]
            num=1,[T,T,T,F]
            num=2,[T,T,T,T], return
        '''
        total = sum(nums)
        if total % 2:
            return False
        n = len(nums)
        goal = total//2
        memo = [False]*(goal+1)
        memo[0] = True
        for num in nums:
            for cur_sum in range(goal, num-1, -1):
                # to achieve cur_sum, either itself achievable(not pick cur)
                # or pick number to build
                memo[cur_sum] = memo[cur_sum] or memo[cur_sum-num]
            if memo[goal]:
                return True
        return memo[goal]

    def canPartition(self, nums: list[int]) -> bool:
        '''
        bitmask(similar to set)
        the core idea: whatever can retrieve state[cur_num,build_sum]
        ith digit: if i is reachable as a sum
        build up reachable sum
        (initial: 0 is reachable) 
        shift means: 
            every already exist sum(e,g, cur_sum=2, num=1), can extend by picking cur number
            101(2 and 0 reachable) -> 1111(3,2,1,0 reachable)
        quite similar to set
        operator priority:
        ~(NOT)
        <<, >>
        &
        ^(XOR)
        |(OR)
        '''
        total = sum(nums)
        if total % 2:
            return False
        n = len(nums)
        goal = total//2
        bitset = 1
        for num in nums:
            pick = bitset << num  # build by adding cur
            bitset |= pick
            if bitset & 1 << goal:
                return True

        return True if bitset & 1 << goal else False


t = [1, 1, 2, 2]
# t = [1, 2, 2]
t = [1, 5, 5, 11]
# t = [10, 2, 8]
t = [1, 2, 3, 5, 17, 6, 14, 12, 6]
t = [1, 2, 5]
r = Solution().canPartition(t)
print(r)
