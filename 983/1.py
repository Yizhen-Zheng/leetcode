class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        '''
        O(3^N), can calculate answer, but has memory limit exceed issue
        '''
        res = []
        self.helper(0, 0, days, costs, res)
        print(res)
        return min(res)

    def helper(self, currentCost: int, currentDayIdx: int, days: list[int], costs: list[int], res: list[int]) -> None:
        if currentDayIdx >= len(days):
            res.append(currentCost)
            return
        nextDays = [0, 0, 0]
        self.helper(currentCost+costs[0], currentDayIdx+1, days, costs, res)
        i = currentDayIdx
        while i < len(days):
            if days[i] >= days[currentDayIdx]+7:
                break
            i += 1
        self.helper(currentCost+costs[1], i, days, costs, res)
        while i < len(days):
            if days[i] >= days[currentDayIdx]+30:
                break
            i += 1
        self.helper(currentCost+costs[2], i, days, costs, res)


t1 = ([1, 4, 7, 40], [2, 7, 15])
t2 = ([1, 4, 7, 40], [2, 7, 15])
t3 = ([1, 7, 8, 40], [7, 2, 15])
t4 = ([1, 4, 6, 7, 8, 20], [7, 2, 15])
t5 = ([1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 27, 28, 29, 30, 31, 34, 37, 38, 39, 41, 43,
       44, 45, 47, 48, 49, 54, 57, 60, 62, 63, 66, 69, 70, 72, 74, 76, 78, 80, 81, 82, 83, 84, 85, 88, 89, 91, 93, 94, 97, 99], [9, 38, 134])
# r1 = Solution().mincostTickets(days=t1[0], costs=t1[1])
# r2 = Solution().mincostTickets(days=t2[0], costs=t2[1])
# r3 = Solution().mincostTickets(days=t3[0], costs=t3[1])
# r4 = Solution().mincostTickets(days=t4[0], costs=t4[1])
r4 = Solution().mincostTickets(days=t5[0], costs=t5[1])
print(r4)
