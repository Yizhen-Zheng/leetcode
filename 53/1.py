from typing import List
from math import inf
'''
kadane algorith:
if current elem > 0, current sum > 0 -> extend 
if current elem > 0, current sum < 0 -> reset 
if current elem < 0, current sum > 0 -> extend 
if current elem < 0, current sum < 0 -> reset 
'''


class Solution:
    def maxSubArrayI(self, nums: List[int]) -> int:
        '''
        brute force
        '''
        n = len(nums)
        maximum = float('-inf')
        dp = [[None]*n for _ in range(n)]
        for l in range(n-1, -1, -1):
            for r in range(l, n):
                if l == r:
                    cur = nums[l]
                else:
                    cur = nums[r]+dp[l][r-1]
                dp[l][r] = cur
                maximum = max(cur, maximum)
        return maximum

    def maxSubArray_rec(self, nums: List[int]) -> int:
        '''
        somehow the '0 if must_pick' correspondes to 'reset' the'prev max' we've accumulated in Kadane's
        which means we start picking from current newly
        '''
        def solve(i, must_pick):
            if i >= len(nums):
                return 0 if must_pick else float('-inf')
            # max of: either include current elem, or end here(the prev rec will consume current solve as 0),
            # or skip current and start choosing next choice's first elem
            return max(nums[i]+solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)

    def maxSubArray_rec_dp(self, nums: List[int]) -> int:
        def solve(dp, i, must_pick):
            if i >= len(nums):
                return 0 if must_pick else float('-inf')
            if dp[must_pick][i]:
                return dp[must_pick][i]
            return max(nums[i]+solve(dp, i+1, True), 0 if must_pick else solve(dp, i+1, False))

        dp = [[None]*len(nums)for _ in range(2)]
        return solve(dp, 0, False)

    def maxSubArray_rec_dp_tabuI(self, nums: List[int]) -> int:
        dp = [[float('-inf')]*len(nums)for _ in range(2)]
        for i in range(0, len(nums)):
            # include current, or start from current
            dp[0][i] = max(dp[0][i-1]+nums[i], nums[i]) if i > 0 else nums[i]
            # max seen so far, of new
            dp[1][i] = max(dp[0][i], dp[1][i-1]) if i > 0 else nums[i]
        return dp[-1][-1]

    def maxSubArray_rec_dp_tabu(self, nums: List[int]) -> int:
        dp = [float('-inf')]*len(nums)
        max_record = float('-inf')
        for i in range(0, len(nums)):
            # include current, or start from current
            dp[i] = max(dp[i-1]+nums[i], nums[i]) if i > 0 else nums[i]
            # max seen so far, of new
            max_record = max(max_record, dp[i-1]) if i > 0 else nums[i]
        return max_record

    def maxSubArray_kadane(self, nums: List[int]) -> int:
        max_record = float('-inf')
        cur_max = 0
        for i in range(0, len(nums)):
            cur_max = max(nums[i], cur_max+nums[i])
            max_record = max(max_record, cur_max)
        return max_record

    def maxSubArray_divide(self, nums: List[int]) -> int:
        '''
        1: best case exists in left half
        2: best case exists in right half
        3: best case combines right and left
        O(n logn) 
            n: every layer, loop nums for finding combined case
            logn: recursion depth
        space : logn
        '''
        def divide(nums, L, R):
            if L > R:
                return -inf
            mid, left_sum, right_sum, cur_sum = (L+R)//2, 0, 0, 0
            for i in range(mid-1, L-1, -1):
                cur_sum += nums[i]
                left_sum = max(left_sum, cur_sum)
            cur_sum = 0
            for i in range(mid+1, R+1):
                cur_sum += nums[i]
                right_sum = max(right_sum, cur_sum)
            return max(divide(nums, L, mid-1), divide(nums, mid+1, R), left_sum+nums[mid]+right_sum)
        return divide(nums, 0, len(nums)-1)

    def maxSubArray_divide_optimize(self, nums: List[int]) -> int:
        '''
            1: best case exists in left half
            2: best case exists in right half
            3: best case combines right and left
            O(n + logn=>n) 
                n: loop nums for finding combined case twice
                logn: recursion depth
            space : logn + n
            origin: 3  2  -5  1  -5
            pre:    3->5->0 ->1->-4
            suf:    5<-2<--4<-1<--5
            (keep prev or reset from itself(by add 0))
            pre[i]: from 0(flexible) to i(fixed), max sum
            suf[i]: from -1(flexible) to i(fixed), max sum
            prev[mid]: from mid, how far we can extend to 0
            suf[mid+1]: from mid+1, how far we can extend to -1
            '''
        pre, suf = [*nums], [*nums]
        for i in range(1, len(nums)):
            pre[i] += max(pre[i-1], 0)

        for i in range(len(nums)-2, -1, -1):
            suf[i] += max(suf[i+1], 0)

        def divide(nums, L, R):
            if L == R:
                return nums[L]
            mid = (L+R)//2
            return max(divide(nums, L, mid), divide(nums, mid+1, R), pre[mid]+suf[mid+1])

        return divide(nums, 0, len(nums)-1)


t = [0]
t = [10, -200, 9, -10]
r = Solution().maxSubArray_divide_optimize(t)
# r = Solution().maxSubArray_rec_dp_tabu(t)
print(r)
