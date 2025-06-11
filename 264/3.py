class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        use 3 pointers
        '''
        hq = [1]
        pointer_2 = 0
        pointer_3 = 0
        pointer_5 = 0

        for i in range(n):
            if i == n-1:
                break
            product_2 = hq[pointer_2]*2
            product_3 = hq[pointer_3]*3
            product_5 = hq[pointer_5]*5
            smallest = min([product_2, product_3, product_5])
            hq.append(smallest)
            if smallest == product_2:
                pointer_2 += 1
            if smallest == product_3:
                pointer_3 += 1
            if smallest == product_5:
                pointer_5 += 1
        return hq


# t = 6
# t = 7
# t = 13
# t = 14
t = 3
r = Solution().nthUglyNumber(t)
print(r)
