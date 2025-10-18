class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        '''
        9:29-9:43 15min
        the tree is like n * (n-1) * ...1 <--only one choice for the last position
        '''
        nums.sort()
        n = len(nums)
        ans = []

        def dfs(path: list[int]):
            if len(path) == n:
                ans.append(path[:])
                return
            for i in range(0, n):
                if nums[i] == None:
                    continue
                if i > 0 and nums[i] == nums[i-1]:
                    continue  # prune
                path.append(nums[i])
                nums[i] = None
                dfs(path)
                nums[i] = path.pop()
        dfs([])
        return ans

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        '''
        iterative solution
        like to breed the perms
        by insertion,
        the tree is like 1 * 2 * ... (n-1) * n <--only one choice for the first position
        so by pruning the branches close to root, effectively reduce the dup
        '''
        ans = [[]]

        for elem in nums:  # like a bfs, idx means tree depth
            new_paths = []
            for path in ans:
                for insert_idx in range(len(path)+1):
                    new_paths.append(path[:insert_idx]+[elem]+path[insert_idx:])
                    if insert_idx < len(path) and path[insert_idx] == elem:
                        break
            ans = new_paths
        return ans


t = [1, 1, 2]
t = [1, 2, 1, 1]
r = Solution().permuteUnique(t)
print(r)
