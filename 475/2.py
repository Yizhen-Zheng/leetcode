import math
import itertools

# memory limit exceeded


class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        '''
        distance: arr[i] - arr[j]
        e.g:
        houses = [1,2,3,4], then h[2] - h[1] = 1
        method2 - hash:
        map houses, heaters array position into idx
        get the max distance
        '''

        length = 1+max(max(houses), max(heaters))
        nums = list(itertools.repeat(-1, length))
        for house in houses:
            nums[house] = 0
        for heater in heaters:
            nums[heater] = 1
        # for each 0, find the nearest 1
        max_r = 0
        l = 0
        r = 0
        idx = 1
        while idx < length:
            if nums[idx] == 0:
                l = r = idx
                while nums[l] != 1 and nums[r] != 1:
                    l = max(1, l-1)
                    r = min(length-1, r+1)
                if nums[r] == 1:
                    max_r = r-idx
                    idx += max_r*2
                else:
                    max_r = idx-l
                print(max_r)
            elif idx == 1:
                idx += max_r
            idx += 1

        print(nums)
        return max_r


t1 = ([1, 2, 3], [2])
t2 = ([1, 2, 3, 4], [1, 4])
t3 = ([282475249, 622650073, 984943658, 144108930,
      470211272, 101027544, 457850878, 458777923], [823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 441282327, 16531729, 823378840, 143542612])
t4 = ([1, 2], [5])
t5 = ([1, 5], [2])
t6 = ([1], [1, 2, 3, 4])
res = Solution().findRadius(t1[0], t1[1])
# res = Solution().findRadius(t2[0], t2[1])
# res = Solution().findRadius(t3[0], t3[1])
# res = Solution().findRadius(t4[0], t4[1])
# res = Solution().findRadius(t5[0], t5[1])
# res = Solution().findRadius(t6[0], t6[1])
# mylist = [1, 2]

print(res)
