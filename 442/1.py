class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        '''
        1<=nums[i]<=n
        n==len
        that means we can leverage idx
        '''
        n = len(nums)
        ans = []
        for i in range(n):
            target_idx = abs(nums[i])-1
            if nums[target_idx] < 0:
                ans.append(target_idx+1)
            nums[target_idx] = -nums[target_idx]
        return ans


t = [2, 2]
t = [1, 1]
t = [1, 2]
t = [1, 2, 3, 3, 1]
r = Solution().findDuplicates(t)
print(r)
