class Solution:
    def __init__(self):
        self.durations = [1, 7, 30]

    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        '''
        memoization db recursive
        res: a table, idx coresoonding with days' idx
        pay for tomorrow(future coming travel), and jump to the day when current ticket expires
        so the out of ranged day needs pay 0, bcz we've already paid
        '''
        res = [float('inf')]*len(days)
        return self.helper(days, costs, res, 0)

    def helper(self, days: list[int], costs: list[int], res: list[int], current_idx: int) -> int:
        if current_idx >= len(days):
            return 0
        if res[current_idx] != float('inf'):
            return res[current_idx]

        for k in range(0, 3):
            j = current_idx
            while j < len(days) and days[j] < days[current_idx] + self.durations[k]:
                j += 1
            current_cost = self.helper(days, costs, res, j)
            res[current_idx] = min(res[current_idx], costs[k]+current_cost)

        return res[current_idx]


t1 = ([1, 4, 7, 40], [2, 7, 15])
t2 = ([1, 4, 7, 40], [2, 7, 15])
t3 = ([1, 7, 8, 40], [7, 2, 15])
t4 = ([1, 4, 6, 7, 8, 20], [7, 2, 15])
t5 = ([1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 27, 28, 29, 30, 31, 34, 37, 38, 39, 41, 43,
       44, 45, 47, 48, 49, 54, 57, 60, 62, 63, 66, 69, 70, 72, 74, 76, 78, 80, 81, 82, 83, 84, 85, 88, 89, 91, 93, 94, 97, 99], [9, 38, 134])
# r = Solution().mincostTickets(days=t1[0], costs=t1[1])
# r = Solution().mincostTickets(days=t2[0], costs=t2[1])
r = Solution().mincostTickets(days=t3[0], costs=t3[1])
# r = Solution().mincostTickets(days=t4[0], costs=t4[1])
# r = Solution().mincostTickets(days=t5[0], costs=t5[1])
print(r)
