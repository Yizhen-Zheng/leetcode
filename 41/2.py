class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        '''
        You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
        Use 2 pointers
        basic idea: use index to mark (or take memo) of number
        [3,-4,9,2,1,6]
        worst case: 
        len = 3
        nums = [1,2,3]
        r = len - 1 = 2
        res = r + 2 = (r + 1) + 1  -> use while l <= r, so when exits the loop, l is r + 1
        every number greater than length will not be considered
        edge: [1] -> eventually: l = 1, return l+1
        edge: [0] -> eventually: l = 0, return l+1
        edge: [2] -> eventually: l = 0, return l+1

        '''
        def swap(l, r):
            '''swap nums in given idx'''
            if l == r:
                return
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp

        length = len(nums)
        l = 0
        r = length-1
        while l <= r:
            if nums[l] == l+1:
                l += 1
            elif nums[l] <= l or nums[l] > r+1 or nums[l] == nums[nums[l]-1]:
                # elif nums[l] <= l or nums[l] > r+1 or nums[l] == nums[nums[l]-1]:
                '''
                don't need value, shrink the search range
                elif nums[l] < 1 or nums[l] > r+1 or nums[l] == nums[nums[l]-1]:  <---this also works, 
                because the missed case would be captured by nums[l] == nums[nums[l]-1] later
                however, elif nums[l] <= l or nums[l] > r+1  not work, 
                because there're potential forward duplications [1,3,3,3] (3 occures before its correct position)
                nums[l] <= l can only cover backward duplications [1,2,2] (2 occures after its correct position)
                forward duplications that nums[l] <= l cannot handle: when the num that has duplicate already at its position
                [1,3,3,2], [3,3,1,2](<-- becomes [1,3,3,2])
                or think of it as proactive / reactive
                '''
                swap(l, r)
                r -= 1
            elif nums[l]-1 <= r:
                '''need the value, put value to corresponding idx'''
                swap(l, nums[l]-1)

        return l+1


t1 = [1, 2, 0]
t2 = [7, 2, 0]
t3 = [1, 2, -1]
t4 = [-1]
t5 = [2]
t6 = [3, 4, -1, 1]
t7 = [2, 1]
s = Solution().firstMissingPositive(t6)
print(s)
