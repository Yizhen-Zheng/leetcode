class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        '''
        brute force: O(n^2), for every elem, loop the arr to check
        map visited using minus
        the input proof to have at least 2 elems(since n >=1, to len(nums)>=2)
        '''
        l = len(nums)
        for i in range(l):
            target_idx = abs(nums[i])-1
            if nums[target_idx] < 0:
                return abs(nums[i])
            nums[target_idx] = -nums[target_idx]

    def findDuplicate(self, nums: list[int]) -> int:
        '''
        find circle
        since n+1 length and n nums, there won't be [1,2,3,5,5], 
        so 2 ptr is safe
        why init with already 1 step: to maintain the while loop 
        consider the s, f as the idx we've traveled, not the value in arr
        '''
        s = nums[0]
        f = nums[nums[0]]
        while s != f:
            s = nums[s]
            f = nums[nums[f]]
        '''  
        above is equal to:    
        which both s and f start exactly from 0  
        s, f = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        '''
        s = 0
        # s = nums[0] <-this is position mismatch
        # we need s start from exactly 0th, not nums[0], which is the second elem in the arr
        while s != f:
            s = nums[s]
            f = nums[f]
        return f


t = [1, 1]
# t = [2, 1, 1]
# t = [3, 2, 1, 4, 3]
t = [1, 3, 4, 2, 5, 2]
r = Solution().findDuplicate(t)
print(r)
