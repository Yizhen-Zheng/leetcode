class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        '''
        with additional space: add, loop hashmap
        10:41- 10:46 
        '''
        majority = None
        count = 0
        for num in nums:
            if num == majority:
                count += 1
            else:
                if count == 0:
                    majority = num
                    count += 1
                else:
                    count -= 1
        return majority

    def majorityElement(self, nums: list[int]) -> int:
        '''
        clean up
        '''
        majority = None
        count = 0
        for num in nums:
            if count == 0:
                majority = num
            if num == majority:
                count += 1
            else:
                count -= 1
        return majority
