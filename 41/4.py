class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        '''
        brute force:(with O(n)spcae)
        create a 10^5 arr, for every elem map it as 'seen'. then iterate from beginning

        '''
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            cur_num = nums[l]
            if cur_num == l+1:
                l += 1
            elif l + 1 < cur_num <= r+1 and nums[cur_num-1] != cur_num:
                # not considered garbage yet, and not duplicated
                # swap so cur_num now is on its correct position
                nums[l], nums[cur_num-1] = nums[cur_num-1], nums[l]
            else:
                # cur_num < l+1 or cur_num > r+1 or duplicated
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
        return l+1


t = [0]
t = [2, 2, 1]
# t = [10]
# t = [1]
# t = [1, 2]
# t = [0, -1, -2]
# t = [3, 4, -1, 1]
# t = [1, 0, 2, 3]
r = Solution().firstMissingPositive(t)
print(r)
