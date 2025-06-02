import math


class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        '''
        distance: arr[i] - arr[j]
        e.g:
        houses = [1,2,3,4], then h[2] - h[1] = 1
        method1 - force brute:
        map house array into house to distance to nearest heaters
        get the max distance
        N * N * logN
        '''
        houses = sorted(houses)
        heaters = sorted(heaters)
        max_distance = 0
        for house in houses:
            heater_position = self.find_nearest_heater(house, heaters)
            distance = abs(heater_position-house)
            max_distance = max(max_distance, distance)
        # for each house, radius = house_position - heater_position
        # get max radius
        return max_distance

    def find_nearest_heater(self, house: int, heaters: list[int]) -> int:
        '''
        find the nearest heater for a house, return the element that represents the heater in heater array
        method1: min(heater, key=lambda d: abs(d-house))
        method2: binary search
        '''
        if house in heaters:
            return house
        elif house > heaters[-1]:
            return heaters[-1]
        elif house < heaters[0]:
            return heaters[0]
        else:
            (l, r) = self.binary_search(house, heaters)
            return min(heaters[l], heaters[r], key=lambda h: abs(h-house))
            # compare left and right, return the one with smaller dist

    def binary_search(self, house: int, heaters: list[int]) -> set[int]:
        l = 0
        r = len(heaters)-1
        while l < r-1:
            mid = math.floor((l+r)/2)
            if heaters[mid] < house:
                l = mid
            else:
                r = mid
        return (l, r)

        # (houses, heaters)
t1 = ([1, 2, 3], [2])
t2 = ([1, 2, 3, 4], [1, 4])
t3 = ([282475249, 622650073, 984943658, 144108930,
      470211272, 101027544, 457850878, 458777923], [823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 441282327, 16531729, 823378840, 143542612])
res = Solution().findRadius(t3[0], t3[1])
print(res)
