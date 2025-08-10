class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        '''
        brute-force:
            I, multiply all, then divide by itself, O(n)
            II, without division, O(n^2)
            III, use bit manipulation
        duplicated calculate: multiply all other elems except itself
        9:08-9:45, debug -9:52
        44min
        t O(n)
        s O(n)
        '''
        n = len(nums)
        prefix = [1]*n
        sufix = [1]*n
        # pre fix
        for i in range(1, n):
            prefix[i] = nums[i-1]*prefix[i-1]
        # sufix
        for i in range(n-2, -1, -1):
            sufix[i] = nums[i+1]*sufix[i+1]
        for i in range(0, n):
            sufix[i] = sufix[i]*prefix[i]
        return sufix

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        '''
        try optimize space
        9:53-10:07, 14min
        '''
        n = len(nums)
        prefix = [1]*n
        # prefix
        for i in range(1, n):
            prefix[i] = nums[i-1]*prefix[i-1]
        # sufix
        prev_num = nums[-1]
        nums[-1] = 1
        for i in range(n-2, -1, -1):
            cur_num = nums[i]
            nums[i] = prev_num*nums[i+1]
            prev_num = cur_num
        print(nums)
        for i in range(0, n):
            prefix[i] = nums[i]*prefix[i]
        return prefix

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        '''
        solusion, space optimized
        '''
        n = len(nums)
        ans = [1]*n
        # prefix
        carry = 1
        for i in range(0, n):
            ans[i] = carry
            carry *= nums[i]
        # sufix
        carry = 1
        for i in range(n-1, -1, -1):
            ans[i] *= carry
            carry *= nums[i]
        return ans


t = [1, 2, 3, 4]
r = Solution().productExceptSelf(t)
print(r)
