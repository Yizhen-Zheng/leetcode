class Solution:
    def fib(self, n: int) -> int:
        '''note: memoization is also near O(n) '''
        a = 0
        b = 1
        idx = 2

        if n <= 1:
            return n
        while idx < n:
            if idx % 2 == 0:
                a = a+b
            else:
                b = a+b
            idx += 1

        return a+b


t1 = 1
t2 = 3

# res = Solution().fib(t1)
res = Solution().fib(t2)
print(res)
