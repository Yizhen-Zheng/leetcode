class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        '''
        about 7 min + debug 1min (forgot call dfs...)
        t: O(n! * n), n factorial! (n! > 2^n for n >=4)
        '''
        ans = []
        n = len(nums)

        def dfs(path: list[int]):
            if len(path) == n:
                ans.append(path[:])
            for i in range(n):
                if nums[i] == None:
                    continue
                path.append(nums[i])
                nums[i] = None
                dfs(path)
                nums[i] = path.pop()
        dfs([])
        return ans

    def permute(self, nums: list[int]) -> list[list[int]]:
        '''
        swap solution
        i:be like the rest spaces
        '''
        ans = []
        n = len(nums)

        def dfs(i: int):
            if i == n:
                ans.append(nums[:])
                return
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        dfs(0)
        return ans


nums = [1, 2, 3]
r = Solution().permute(nums)
print(r)
