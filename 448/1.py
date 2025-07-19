class Solution:
    def findDisappearedNumbersI(self, nums: list[int]) -> list[int]:
        '''
        hash
        [1,n], no negative elem
        '''
        for num in nums:
            target_idx = abs(num)-1
            nums[target_idx] = -abs(nums[target_idx])
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans

    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        '''
        cycle sort
        [1,n], no negative elem
        '''
        n = len(nums)
        ans = []
        for i in range(n):
            cur_num = nums[i]
            while cur_num != i+1 and nums[cur_num-1] != cur_num:
                nums[i], nums[cur_num-1] = nums[cur_num-1], nums[i]
                cur_num = nums[i]

        for i in range(n):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans
