
class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        '''
        distance: arr[i] - arr[j]
        e.g:
        houses = [1,2,3,4], then h[2] - h[1] = 1
        method3 - 

        N * N * logN
        '''
        houses.sort()
        heaters.sort()
        max_r = 0
        current_r = 0
        current_heater = 0

        for house in houses:

            while current_heater < len(heaters)-1 and house >= heaters[current_heater]:
                current_heater += 1
                # house wil <= current heater
            if abs(heaters[current_heater] - house) <= abs(house - heaters[max(current_heater-1, 0)]):
                current_r = abs(heaters[current_heater] - house)
            else:
                current_r = abs(house-heaters[current_heater-1])

            max_r = max(max_r, current_r)

        # for each house, radius = house_position - current_heater
        # get max radius

        return max_r


t1 = ([1, 2, 3], [2])
t2 = ([1, 2, 3, 4], [1, 4])
t3 = ([1], [1, 2, 3, 4])
t4 = ([1, 5], [10])
t5 = ([1], [2])
t6 = ([2], [1])

# res = Solution().findRadius(t1[0], t1[1])
# res = Solution().findRadius(t2[0], t2[1])
# res = Solution().findRadius(t3[0], t3[1])
# res = Solution().findRadius(t4[0], t4[1])
# res = Solution().findRadius(t5[0], t5[1])
res = Solution().findRadius(t6[0], t6[1])
# res = Solution().findRadius(t7[0], t7[1])
print(res)
