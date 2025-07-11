from typing import List


class Solution:
    def reversePairsI(self, nums: List[int]) -> int:
        '''
        check: i < j and nums[i]>nums[j]
        if we find they sorted, then we only need to compare the value 
        because their position are going to be fixed(or, irrelavant)
        if they're originally sorted ascending order, then just return 0
        where changing inner order does not effect on outer result
        and get convenience after sorting
        '''
        def merge(nums, l, m, r) -> list[int]:
            merged = []
            lptr = l
            rptr = m
            while lptr < m and rptr < r:
                if nums[lptr] < nums[rptr]:
                    merged.append(nums[lptr])
                    lptr += 1
                else:
                    merged.append(nums[rptr])
                    rptr += 1

            merged.extend(nums[lptr:m])
            merged.extend(nums[rptr:r])

            nums[l:r] = merged
            return

        def compare(nums, l, m, r) -> int:
            count = 0
            # compare
            lptr = l
            rptr = m
            prev = 0
            while lptr < m:
                while rptr < r and nums[lptr] > nums[rptr]*2:
                    prev += 1
                    rptr += 1
                count += prev
                lptr += 1
            merge(nums, l, m, r)
            return count
        n = len(nums)
        ans = 0
        unit_len = 1
        # from unit = 1
        while unit_len < n:
            for i in range(0, n, unit_len << 1):
                l = i
                m = min(i+unit_len, n)
                r = min(m+unit_len, n)
                new_count = compare(nums, l, m, r)
                ans += new_count
            unit_len <<= 1
        return ans

    def reversePairs(self, nums: List[int]) -> int:

        def merge(nums, l, m, r) -> list[int]:
            merged = []
            lptr = l
            rptr = m+1
            while lptr < m+1 and rptr < r+1:
                if nums[lptr] < nums[rptr]:
                    merged.append(nums[lptr])
                    lptr += 1
                else:
                    merged.append(nums[rptr])
                    rptr += 1

            merged.extend(nums[lptr:m+1])
            merged.extend(nums[rptr:r+1])

            nums[l:r+1] = merged
            return

        def compare(nums, l, m, r) -> int:
            count = 0
            # compare
            lptr = l
            rptr = m+1
            prev = 0
            while lptr < m+1:
                while rptr < r+1 and nums[lptr] > nums[rptr]*2:
                    prev += 1
                    rptr += 1
                count += prev
                lptr += 1
            merge(nums, l, m, r)
            return count

        def rec(nums, l, r):
            if l == r:
                return 0
            m = (l+r)//2
            left_count = rec(nums, l, m)
            right_count = rec(nums, m+1, r)
            merged_count = compare(nums, l, m, r)
            return left_count+right_count+merged_count
        return rec(nums, 0, len(nums)-1)


t = []
t = [1, 2]
# t = [3, 1]
t = [3, 4, 1]
r = Solution().reversePairs(t)
print(r)
