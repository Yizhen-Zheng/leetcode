class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        '''
        15:43-15:48, debug
        5min
        remove duplicated
        given nums are unique
        the subset itself can in any order
        n=len
        t: O(2^n)(subset number)
        s: O(1)(ans has sO(2^n))
        '''
        ans = [[]]
        for elem in nums:
            todo = len(ans)
            for i in range(todo):
                ans.append(ans[i]+[elem])
        return ans

    def subsets(self, nums: list[int]) -> list[list[int]]:
        '''
        use bit set to generate all possible combinations(use idx as elem, not nums themselves):
        from [0,0,...0] to [1,1,...1]
        t: O(2^n)(subset number)
        s: O(1)
        '''
        n = len(nums)
        res = []
        for i in range(1 << n):  # generate all possible combinations
            subset = []
            for j in range(n):
                if i & (1 << j):  # current combination has idx i
                    subset.append(nums[j])
            res.append(subset)
        return res

    def subsets(self, nums: list[int]) -> list[list[int]]:
        '''
        dfs
        '''
        res = []
        n = len(nums)
        path = []

        def dfs(idx):
            if idx == n:  # finished one path
                res.append(path.copy())
                return
            # pick cur:
            path.append(nums[idx])
            dfs(idx+1)
            # remove cur
            path.pop()
            # skip cur:
            dfs(idx+1)   # build path without cur

        dfs(0)
        return res


t = [1, 2, 3]
r = Solution().subsets(t)
print(r)
