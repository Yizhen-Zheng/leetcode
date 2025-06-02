class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        '''
        space: O(1)
        '''
        print(nums)
        # the numbers pointers contains are idx, not the elements in nums
        # Thus from 0, ...
        # already have the first step before loop
        f = nums[nums[0]]
        s = nums[0]
        # while they don't have the same index(mean haven't meet)
        while f != s:
            s = nums[s]
            f = nums[nums[f]]
        # back to 0 (init point)
        f = 0
        while f != s:
            f = nums[f]
            s = nums[s]
        # we have M * (b + c) + c = a
        # from 2 * (a + b) = a + N * (b + c), where N = M + 1
        # and Because ptr A from 0, ptr B from meet point
        # if B travels M * (b + c) + c, B will end at Entry point
        # if A travels distance of a; A will use the same time as B and end at the same (Entry point)
        # no matter what number N, M are,
        # the existing of c proofs B would reach the entry point at the same time as A travels a distance of a ,
        print('f:{f}, s:{s}'.format(f=f, s=s))
        return f


t1 = [1, 3, 4, 2, 2]
# idx:
# 0-1-3-2-4-2
s = Solution().findDuplicate(t1)
