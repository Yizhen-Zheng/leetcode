from collections import defaultdict


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        idx: i!=j!=k
        not duplicated combinations
        brute force: n**3, i in (0,n-2), j in (i+1,n-1), k in (j+1,n) to prevent duplication
        problem: get duplicated val 
        how to retrive value more efficiently?
        should deal with multiple position with same value
        sort?
        14min not solved
        tuple can be key of dict, and can compare
        additional 5 min to hash seen
        t: O(n^3)
        s: O(n^3)(potentially all tuples)
        '''
        n = len(nums)
        val_to_idx = defaultdict(list)
        seen = set()
        ans = []
        for i in range(n):
            val_to_idx[nums[i]].append(i)
        for i in range(n-2):
            a = nums[i]
            for j in range(i+1, n-1):
                b = nums[j]
                for k in range(j+1, n):
                    c = nums[k]
                    if a+b+c == 0 and tuple(sorted([a, b, c]))not in seen:
                        ans.append([a, b, c])
                        seen.add(tuple(sorted([a, b, c])))
        print(val_to_idx)
        return ans

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        sort, 2 ptr for every start val
        problem: use hash table to prevent duplication
        cannot skip producing duplications 
        30min
        '''
        # num_to_idx = []
        # for i in range(n):
        #     num_to_idx.append((nums[i], i))
        # num_to_idx.sort(key=lambda x: x[0])
        n = len(nums)
        nums.sort()
        seen = set()

        for i in range(0, n-2):
            a = nums[i]
            if a <= 0:
                j, k = i+1, n-1
                while j < k and nums[k] >= 0:  # between i+1 and n-1 there can be multiple solution
                    if a+nums[j]+nums[k] == 0:
                        b, c = nums[j], nums[k]
                        if (a, b, c)not in seen:
                            seen.add((a, b, c))
                        j += 1
                    elif a+nums[j]+nums[k] < 0:
                        j += 1
                    else:
                        k -= 1

        return list(seen)

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''

        '''
        n = len(nums)
        nums.sort()
        res = []
        for i in range(0, n-2):
            while i != 0 and nums[i] != nums[i-1] and nums[i] > 0:
                continue
            if i == 0 or nums[i] != nums[i-1]:
                j, k = i+1, n-1
                while j < k and nums[k] >= 0:  # between i+1 and n-1 there can be multiple solution
                    if nums[i]+nums[j]+nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        j += 1
                        while j < k and nums[j-1] == nums[j]:
                            j += 1
                    elif nums[i]+nums[j]+nums[k] < 0:
                        j += 1
                    else:
                        k -= 1
        return res


t = [-1, 0, 1, 2, -1, -4]
# t = [-2, 0, 1, 1, 2]
r = Solution().threeSum(t)
print(r)
