class Solution:
    def maxArea(self, height: list[int]) -> int:
        '''
        10min
        it can be solved in DP, but time O(n^2) (as there're 2 variables)
        (all combinations of l and r)
        '''
        n = len(height)
        l, r = 0, n-1
        max_vol = 0
        while l < r:
            cur_vol = (r-l)*min(height[l], height[r])
            max_vol = max(max_vol, cur_vol)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_vol
