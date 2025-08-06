import heapq


class MedianFinder:

    def __init__(self):
        '''
        brute-force: if store all val, insert will be O(n)
        seems inputs are not sorted
        heap: small top
        30min
        time:O(logn)
        space:O(n)
        '''
        # len(l) >= len(r)
        self.left = []  # negative val(biggist at top of heap)
        self.right = []  # positive

    def addNum(self, num: int) -> None:
        # another concise way to maintain structure, reduce edge cases
        heapq.heappush(self.left, -num)
        # if num is bigger than right top, it will natually bubble up to left top
        left_top = -heapq.heappop(self.left)
        heapq.heappush(self.right, left_top)
        if len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))
        return
        print(self.left)
        print(self.right)
        if len(self.left) != len(self.right):  # if len l>r, add to right
            left_top = -self.left[0]
            if num < left_top:  # num smaller than mid, swap
                heapq.heappop(self.left)
                heapq.heappush(self.right, left_top)
                heapq.heappush(self.left, -num)
            else:
                heapq.heappush(self.right, num)
        elif len(self.left) == len(self.right) == 0:
            self.left.append(-num)
        else:  # current len equal, add to left
            right_top = self.right[0]
            if num > right_top:
                heapq.heappop(self.right)
                heapq.heappush(self.left, -right_top)
                heapq.heappush(self.right, num)

            else:
                heapq.heappush(self.left, -num)
        return

    def findMedian(self) -> float:
        print(self.left)
        print(self.right)
        if len(self.left) != len(self.right):  # if odd left, even right
            return -self.left[0]
        else:  # both even
            l = -self.left[0]
            r = self.right[0]
            return (l+r)/2

        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()


def test():
    t = MedianFinder()
    t.addNum(1)
    t.addNum(2)
    t.findMedian()
    t.addNum(3)
    t.findMedian()


test()
