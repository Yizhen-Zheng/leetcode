class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        '''
        10:51-10:53
        '''
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    def containsDuplicate(self, nums: list[int]) -> bool:
        '''
        solution
        '''
        unique = set(nums)
        return True if len(unique) != len(nums) else False
