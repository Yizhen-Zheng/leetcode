class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        review
        2,3,5
        1 2 3 4 5 
        '''
        ugly = [1]
        pointer_a = 0
        pointer_b = 0
        pointer_c = 0
        while len(ugly) < n:
            a = 2 * ugly[pointer_a]
            b = 3 * ugly[pointer_b]
            c = 5 * ugly[pointer_c]
            next_ugly = min(a, b, c)
            ugly.append(next_ugly)
            if next_ugly == a:
                pointer_a += 1
            if next_ugly == b:
                pointer_b += 1
            if next_ugly == c:
                pointer_c += 1

        print(ugly)
        return ugly[-1]


# t = 6
# t = 7
# t = 13
t = 14
# t = 3
r = Solution().nthUglyNumber(t)
print(r)
