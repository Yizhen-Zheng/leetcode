from collections import deque
import heapq


class MedianFinder:
    '''
    ordered int list, pos or neg
    '''

    def __init__(self):
        self.less = []  # top: max
        self.more = []  # top: min

    def addNum(self, num: int) -> None:
        less, more = self.less, self.more

        # mid_l, mid_r = -self.smaller[0], self.greater[0]
        if len(less) == len(more):
            heapq.heappush(less, -num)
        else:
            heapq.heappush(more, num)

        if len(more) > 0:  # bigger part has elem, iow, at least 2 elems total
            if -less[0] > more[0]:  # top distorted
                heapq.heappush(more, -heapq.heappop(less))
                heapq.heappush(less, -heapq.heappop(more))
        return

    def findMedian(self) -> float:
        less, more = self.less, self.more
        m, n = len(less), len(more)
        if m == n:
            return (-less[0]+more[0])/2
        return -less[0]


t = MedianFinder()
t.addNum(1)
t.addNum(2)
t.addNum(3)
