class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        '''
        elem can dup, ans not contain dup
        seems similar to 'skip equivalent parenthesis'
        for a string of identical num, if not choose / add, use which doesn't matter


        brute-force: sort and put into set
        omg?? it passed... about 8-10 min
        '''
        ans = {()}
        n = len(nums)
        for i in range(n):
            new_elems = []
            for elem in ans:
                new_elems.append(tuple(sorted(list(elem)+[nums[i]])))
            ans.update(new_elems)
        return list(map(list, ans))

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        '''
        try non brute force
        watch solution:
        bfs
        prev_size:
        elems that will be 'poluted' by cur
        will be used for next turn to know from where it's not touched by the same elem
        by using size, it started from first not dup elem(like [2]->[2,2])

        '''
        nums.sort()
        ans = [[]]
        n = len(nums)
        for i in range(n):
            s = prev_size if i > 0 and nums[i] == nums[i-1] else 0
            prev_size = len(ans)
            new_elems = []
            for j in range(s, len(ans)):
                new_elems.append(ans[j]+[nums[i]])
            ans.extend(new_elems)
        return ans

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        '''
        watch solution:
        dfs
        pick as usual, when not pick, skip dup
        '''
        nums.sort()
        n = len(nums)
        ans = []

        def dfs(i: int, path: list[int]):
            if i >= n:
                ans.append(path[:])
                return
            path.append(nums[i])  # pick
            dfs(i+1, path)
            path.pop()
            # skip dup
            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, path)
            return
        dfs(0, [])
        return ans

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        '''
        watch solution:
        dfs another way
        pick as usual, when not pick, skip dup
        '''
        nums.sort()
        n = len(nums)
        ans = []

        def dfs(i: int, path: list[int]):
            if i >= n:
                ans.append(path[:])
                return
            # count dup(same as cur)
            j = i
            while j < n and nums[i] == nums[j]:
                j += 1
            dfs(j, path)  # skip all dup including not pick cur
            for dup_idx in range(i, j):
                path.append(nums[dup_idx])
                dfs(j, path)
            for _ in range(i, j):
                path.pop()
            return
        dfs(0, [])
        return ans


t = [1, 2, 3]
t = [1, 2, 2]
r = Solution().subsetsWithDup(t)
print(r)
