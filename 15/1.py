class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        7:29 
        review
        sum to 0
        can dup inside a tuple, but tuples must distinct from each other
        brute force: 
        t O(n^3), enumerate all
        '''
        nums = sorted(nums)
        n = len(nums)
        ans = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i]+nums[j]+nums[k] == 0:
                        # if (nums[i], nums[j], nums[k]) not in ans:
                        ans.add((nums[i], nums[j], nums[k]))
        return list(map(list, ans))

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        NOTE note work
        '''
        def search(l, r, target):
            while l < r:
                m = l+(r-l)//2
                if nums[m] > target:
                    r = m
                elif nums[m] < target:
                    l = m+1
                else:
                    return m
            return -1
        nums = sorted(nums)
        n = len(nums)
        ans = set()
        l, r = 0, n-1
        while l < r-1:
            target = -(nums[l]+nums[r])
            m = search(l, r, target)
            if m != -1 and m != l:
                ans.add((nums[l], nums[m], nums[r]))

            if target < 0:  # r too big
                r -= 1
            else:  # l too small
                l += 1
        return list(map(list, ans))

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        solution
        t: O(n*n)
        s: O(n)
        '''
        res = set()
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)
        N, P = set(n), set(p)
        # neg,0,pos case
        if z:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))
        # 3 zeros case
        if len(z) > 2:
            res.add((0, 0, 0))
        # (n,n,p)
        for neg_i in range(len(n)):
            for neg_j in range(neg_i+1, len(n)):
                target = -(n[neg_i]+n[neg_j])
                if target in P:
                    if n[neg_i] < n[neg_j]:
                        res.add((n[neg_i], n[neg_j], target))
                    else:
                        res.add((n[neg_j], n[neg_i], target))

        # (n,p,p)
        for pos_i in range(len(p)):
            for pos_j in range(pos_i+1, len(p)):
                target = -(p[pos_i]+p[pos_j])
                if target in N:
                    if p[pos_i] < p[pos_j]:
                        res.add((target, p[pos_i], p[pos_j]))
                    else:
                        res.add((target, p[pos_j], p[pos_i]))

        return list(map(list, res))

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        seen = set()

        for i in range(0, n-2):
            a = nums[i]
            if a <= 0:  # at least one elem <=0
                j, k = i+1, n-1
                while j < k and nums[k] >= 0:  # between i+1 and n-1 there can be multiple solution
                    # at least one elem >= 0(k)
                    if a+nums[j]+nums[k] == 0:
                        b, c = nums[j], nums[k]
                        seen.add((a, b, c))
                        j += 1  # go to next
                    elif a+nums[j]+nums[k] < 0:
                        j += 1  # move mid to bigger
                    else:
                        k -= 1  # move pos

        return list(seen)


t = [-1, 0, 1, 2, -1, -4]
# t = [-1, 0, 1]
r = Solution().threeSum(t)
print(r)
