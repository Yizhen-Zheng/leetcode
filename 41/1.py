class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        '''
        You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
        This file does not work. It contains sketchy attempting 
        '''
        missing = 1
        current_smallest = nums[0]
        #
        for n in nums:
            if n <= 0:
                continue
            if n == missing:
                # go to next space that has not been filled
                pass
            current_smallest = min(n, current_smallest)

            if missing > current_smallest:
                missing = current_smallest+1
        return missing
    # smallest_in_nums
    # missing=1
    # update missing, smallest_in_nums when loop


t1 = [1, 2, 0]
t1 = [7, 2, 0]
t1 = [1, 2, -1]
s = Solution().firstMissingPositive(t1)
print(s)
