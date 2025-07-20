class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        '''
        1, cycle sort, then find one with idx mismatching
            or use a normal sort, and find where the idx+1!=nums[idx] first happens, 
            the nums[idx] is duplicated number, 
            then we loop from (1,n), e,g, [1,2,2,3,4], n=5, we cannot find 5 so missing num is 5
                                          [1,2,2,4,5],      no 3, break
            (a normal sort here is not efficient at all XP)
        2, map(time: O(n) space: O(n))
        '''
        n = len(nums)
        dup = None
        miss = None
        hashmap = [0]*(n+1)
        for num in nums:
            hashmap[num] += 1
        for i in range(1, n+1):
            if not hashmap[i]:
                miss = i
            elif hashmap[i] > 1:
                dup = i
        return [dup, miss]

    def findErrorNums(self, nums: list[int]) -> list[int]:
        '''
        time: O(n)
        space: O(n)
        '''
        n = len(nums)
        unique_sum = sum(set(nums))
        all_sum = sum(nums)
        expected_sum = (1+n)*n//2
        miss = expected_sum-unique_sum
        dup = all_sum-unique_sum
        return [dup, miss]

    def findErrorNums(self, nums: list[int]) -> list[int]:
        '''
        cycle sort
        time: O(n)
        space: O(1)
        '''
        n = len(nums)
        i = 0
        for i in range(n):
            cur_num = nums[i]
            while cur_num != i+1 and nums[cur_num-1] != cur_num:  # check where it should go
                nums[i], nums[cur_num-1] = nums[cur_num-1], nums[i]
                cur_num = nums[i]

        for i in range(n):
            if nums[i] != i+1:
                return [nums[i], i+1]

    def findErrorNums(self, nums: list[int]) -> list[int]:
        '''
        if a^b=c:
        c^a=b, c^b=a
        a^a=0
        python does not have a sign bit
        print((-1024)>>31) will give -1
        '''
        n = len(nums)
        xor_expected = 0
        xor_sum = 0
        for i in range(1, n+1):
            xor_expected ^= i
        for num in nums:
            xor_sum ^= num
        xor_result = xor_expected ^ xor_sum  # different -> 1
        right_most_set_bit = xor_result & -xor_result
        xor_set = 0
        xor_not_set = 0

        for i in range(1, n+1):
            if (i & right_most_set_bit) != 0:
                xor_set ^= i
            else:
                xor_not_set ^= i

        for num in nums:
            if (num & right_most_set_bit) != 0:
                xor_set ^= num
            else:
                xor_not_set ^= num
        for num in nums:
            if num == xor_set:
                return [xor_set, xor_not_set]

        return [xor_not_set, xor_set]


t = [1, 1]
# t = [2, 2]
# t = [3, 1, 2, 2]
# t = [4, 1, 2, 2]
# t = [2, 3, 2]
r = Solution().findErrorNums(t)
print(r)
