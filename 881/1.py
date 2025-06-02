class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        '''
        person weights are represented in people[i]
        each boat can carry at most limit weight
        limit is proofed >= people[i]
        at most 2 person on the same boat
        N * log n + n
        greedy + 2 pointer
        '''
        if len(people) == 1:
            return 1
        result = 0
        nums = sorted(people)
        l = 0
        r = len(nums)-1
        while l <= r:
            result += 1
            if (l == r):
                # l and r point to the same person (the last person)
                break
            if nums[l]+nums[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
        return result


t1 = [3, 2, 2, 2]
# 3

res = Solution().numRescueBoats(t1, 3)
print(res)
