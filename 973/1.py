import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        '''
        brute-force: calculate dist, sort dist
        t:O(nlogn)
        s:O(n)
        9 min
        '''
        dists = []
        for x, y in points:
            d = x*x + y*y
            dists.append((d, x, y))
        dists.sort(key=lambda x: x[0])
        ans = list(map(lambda x: [x[1], x[2]], dists[:k]))
        return ans

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        '''
        max-heap
        7-min
        t:O(nlogK) <-heap only has K elem
        s:O(k)
        another trick: 
            implement heap that only replace the top elem, then heapify-down the new elem
            comparing to heapify top elem down, append new, then heapify new elem up
        '''
        ans = []
        for i, (x, y) in enumerate(points):
            d = x*x + y*y
            heapq.heappush(ans, (-d, i))
            if len(ans) > k:
                heapq.heappop(ans)
        ans = list(map(lambda x: points[x[1]], ans))
        return ans

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        '''
        quick-sort
        average should be:
        t:O(n), worst:O(n^2)(choose every elem is O(n), then partition is O(n))
        s:O(1)
        '''
        def compare(p1, p2):
            '''return minus if p1 closer than p2'''
            print(p1, p2)
            x1, y1 = points[p1]
            x2, y2 = points[p2]
            return x1**2 + y1**2 - x2**2 - y2**2

        def partition(low, high):
            # l: always be pivot
            cur, l, r = low, low, high
            while cur <= r:
                delta_d = compare(cur, l)
                if delta_d > 0:  # Dp1>Dpivot
                    # swap cur and larger part
                    points[cur], points[r] = points[r], points[cur]
                    r -= 1
                elif delta_d < 0:
                    # swap cur and smaller part
                    points[cur], points[l] = points[l], points[cur]
                    cur += 1
                    l += 1
                else:
                    cur += 1
            return cur-1
        n = len(points)
        low, high = 0, n-1
        while low < high:
            mid = partition(low, high)
            if mid == k:
                break
            elif mid < k:
                low = mid+1
            else:
                high = mid-1
        return points[:k]


t = ([[1, 3], [-2, 2]], 2)
r = Solution().kClosest(t[0], t[1])
print(r)
