class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        8:21-8:32
        '''
        nums.sort()
        ans = []
        l, r = 0, len(nums)-1
        while l < r-1:
            m = r-1
            while m > l and nums[m]+nums[l]+nums[r] > 0:
                m -= 1
            if nums[m]+nums[l]+nums[r] == 0:
                ans.append([nums[l], nums[m], nums[r]])
            while nums[l+1] == nums[l] and l < r-1:
                l += 1
            while nums[r-1] == nums[r] and l < r-1:
                r -= 1
            if nums[l]+nums[r] < 0:
                l += 1
            else:
                r -= 1
        return ans

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        BF X TLE
        i remember there're a lot of conditions
        slide m until sum<0
        '''
        nums.sort()
        ans = []
        n = len(nums)
        l = 0
        while l < n and nums[l] < 0:
            r = len(nums)-1
            while r > l+1 and nums[r] > 0:
                m = r-1
                while m > l and nums[m]+nums[l]+nums[r] >= 0:
                    if nums[m]+nums[l]+nums[r] == 0:
                        ans.append([nums[l], nums[m], nums[r]])
                        break
                    m -= 1
                r -= 1
                while nums[r] > 0 and nums[r] == nums[r+1]:
                    r -= 1
            l += 1
            while l < n and nums[l] < 0 and nums[l] == nums[l-1]:
                l += 1
        if l+2 < len(nums) and nums[l] == 0 and nums[l+1] == 0 and nums[l+2] == 0:
            ans.append([0, 0, 0])
        return ans

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        t:O(n^2) (2 ptr, upper and lower bound! move ptr to the side that more likely to get ans, avoid the third loop)
        s:O(1)
        '''
        nums.sort()
        n = len(nums)
        ans = []
        for l in range(n):
            if nums[l] > 0:
                break
            if l > 0 and nums[l] == nums[l-1]:
                continue
            m, r = l+1, n-1
            while m < r:
                if nums[l]+nums[m]+nums[r] > 0:
                    r -= 1
                elif nums[l]+nums[m]+nums[r] < 0:
                    m += 1
                else:
                    ans.append([nums[l], nums[m], nums[r]])
                    # skip dup
                    vm, vr = nums[m], nums[r]
                    while nums[m] == vm and m < r:
                        m += 1
                    while nums[r] == vr and r > m:
                        r -= 1
        return ans

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        t:O(n+n^2)
        s:O(n)
        '''
        n, p, z = [], [], []
        ans = []
        for num in nums:
            if num < 0:
                n.append(num)
            elif num > 0:
                p.append(num)
            else:
                z.append(num)
        nset, pset = set(n), set(p)
        if len(z) >= 3:
            ans.append([0, 0, 0])
        n.sort()
        p.sort()
        if len(z) > 0:  # [l,0,r]
            for nnum in nset:
                if -nnum in pset:
                    ans.append([nnum, 0, -nnum])
        # [n,n,p]
        lenn, lenp = len(n), len(p)
        for l in range(lenn):
            if l > 0 and n[l] == n[l-1]:
                continue
            for m in range(l+1, lenn):
                if m > l+1 and n[m] == n[m-1]:
                    continue
                if -(n[l]+n[m]) in pset:
                    ans.append([n[l], n[m], -(n[l]+n[m])])

        # [n,p,p]
        for m in range(lenp):
            if m > 0 and p[m] == p[m-1]:
                continue
            for r in range(m+1, lenp):
                if r > m+1 and p[r] == p[r-1]:
                    continue
                if -(p[m]+p[r]) in nset:
                    ans.append([-(p[m]+p[r]), p[m], p[r]])
        return ans


t = [0, 0, 0]
t = [-1, 0, 0, 0, 0, 1]
# t = [-1, -1, -1, -1,  2]
# t = [-100, -70, -60, 110, 120, 130, 160]
t = [-3, -2, -1]
t = [34, 55, 79, 28, 46, 33, 2, 48, 31, -3, 84, 71, 52, -3, 93, 15, 21, -43, 57, -6, 86, 56, 94, 74, 83, -14, 28, -
     66, 46, -49, 62, -11, 43, 65, 77, 12, 47, 61, 26, 1, 13, 29, 55, -82, 76, 26, 15, -29, 36, -29, 10, -70, 69, 17, 49]
r = Solution().threeSum(t)

print(r)
