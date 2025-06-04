class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        '''
        bottom up
        can use a simple for / while loop, instead of recursive
        '''

        calendar = [0]*366

        def helper(current_day: int, idx: int):
            if current_day > 365 or idx >= len(days):

                return calendar[current_day-1]
            if current_day != days[idx]:
                calendar[current_day] = calendar[current_day-1]
            else:
                idx += 1
                d = calendar[max(current_day-1, 0)]+costs[0]
                w = calendar[max(current_day-7, 0)]+costs[1]
                m = calendar[max(current_day-30, 0)]+costs[2]
                cost = min(d, w, m)
                calendar[current_day] = cost
            return helper(current_day+1, idx)
        res = helper(1, 0)
        print(calendar)
        return res


t1 = ([1, 4, 7, 40], [2, 7, 15])
t2 = ([1, 4, 7, 40], [2, 7, 15])
t3 = ([1, 7, 8, 40], [7, 2, 15])
t4 = ([1, 4, 6, 7, 8, 20], [7, 2, 15])
t5 = ([1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 24, 25, 27, 28, 29, 30, 31, 34, 37, 38, 39, 41, 43,
       44, 45, 47, 48, 49, 54, 57, 60, 62, 63, 66, 69, 70, 72, 74, 76, 78, 80, 81, 82, 83, 84, 85, 88, 89, 91, 93, 94, 97, 99], [9, 38, 134])
# r = Solution().mincostTickets(days=t1[0], costs=t1[1])
# r = Solution().mincostTickets(days=t2[0], costs=t2[1])
# r = Solution().mincostTickets(days=t3[0], costs=t3[1])
# r = Solution().mincostTickets(days=t4[0], costs=t4[1])
r = Solution().mincostTickets(days=t5[0], costs=t5[1])
print(r)
