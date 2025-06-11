class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        use binary heap

        '''
        hq = [1]
        base = [2, 3, 5]
        lookup = {1}

        def insert(n):
            hq.append(n)
            current_pos = len(hq)-1
            while hq[current_pos] < hq[int((current_pos-1)//2)]:
                # swap
                hq[current_pos], hq[int(
                    (current_pos-1)//2)] = hq[int((current_pos-1)//2)], hq[current_pos]
                current_pos = (current_pos-1)//2
            return

        def heap_down():
            current_pos = 0
            while True:
                left = current_pos*2+1
                right = current_pos*2+2
                smallest = current_pos
                if left < len(hq) and (hq[smallest] > hq[left]):
                    smallest = left
                if right < len(hq) and (hq[smallest] > hq[right]):
                    smallest = right

                if current_pos == smallest:
                    break
                hq[current_pos], hq[smallest] = hq[smallest], hq[current_pos]
                current_pos = smallest
            return

        for i in range(n):
            hq[0], hq[len(hq)-1] = hq[len(hq)-1], hq[0]
            smallest_u = hq.pop()
            heap_down()
            if i == n-1:
                return smallest_u
            for u in base:
                new = smallest_u*u
                if new in lookup:
                    continue
                insert(new)
                lookup.add(new)
        return 0


t = 6
t = 7
# t = 13
# t = 14
# t = 3
r = Solution().nthUglyNumber(t)
print(r)
