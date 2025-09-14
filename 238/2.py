
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        '''
        loop
        brute-force: t:O(n**2), s:O(1)
        about 14 min
        '''
        # n = len(nums)
        # ans = [1]
        # for i in range(1, n):
        #     ans.append(ans[-1]*nums[i-1])  # append is using more time
        # acc = 1
        # for i in range(n-2, -1, -1):
        #     acc *= nums[i+1]
        #     ans[i] *= acc
        # return ans
        n = len(nums)
        ans = [1]*n
        for i in range(1, n):
            ans[i] = (ans[i-1]*nums[i-1])  # append is using more time
        acc = 1
        for i in range(n-2, -1, -1):
            acc *= nums[i+1]
            ans[i] *= acc
        return ans
