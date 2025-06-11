import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        use python built-in binary heap

        '''
        hq = [1]
        base = [2, 3, 5]
        lookup = {1}

        for i in range(n):
            smallest_u = heapq.heappop(hq)
            if i == n-1:
                return smallest_u

            for u in base:
                new = smallest_u*u
                if new in lookup:
                    continue
                lookup.add(new)
                heapq.heappush(hq, new)
        return 1


t = 6
# t = 7
# t = 13
# t = 14
t = 3
r = Solution().nthUglyNumber(t)
print(r)
