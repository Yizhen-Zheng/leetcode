class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        '''
        You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
        basic idea: use index to mark (or take memo) of number
        [3,-4,9,2,1,6]
        '''

        length = len(nums)

        for i in range(length):
            if nums[i] < 1:
                nums[i] = length+1
        for i in range(length):
            idx = abs(nums[i])-1
            if idx < length:
                nums[idx] = -abs(nums[idx])
        for i in range(length):
            if nums[i] > 0:
                return i+1
        return length+1


t1 = [1, 2, 0]
t2 = [7, 2, 0]
t3 = [1, 2, -1]
s = Solution().firstMissingPositive(t2)
print(s)
