class Solution:
    def maxArea(self, height: list[int]) -> int:
        '''
        use greedy to move pointers, and keep a memo of most water amount
        '''
        l = 0
        r = len(height)-1
        most_water = 0
        while l < r:
            most_water = max(most_water, (r-l)*min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return most_water


t1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
res = Solution().maxArea(t1)
print(res)
