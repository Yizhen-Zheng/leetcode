class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        min_bound = -(1 << 31)
        max_bound = (1 << 31)-1
        if dividend == min_bound and divisor == min_bound:
            return 1
        elif dividend == min_bound and divisor == -1:
            return max_bound
        # elif dividend == min_bound:
        #     dividend += divisor
        add_one = dividend == min_bound
        negative_res = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        for i in range(31, -1, -1):
            # i=31 this should work since all negative as taken abs, the sign bits are all 0 now
            if ((dividend >> i) >= divisor):
                ans |= (1 << i)
                dividend -= divisor << i
        if negative_res:
            ans = -ans-add_one
        else:
            ans = ans+add_one
        return ans


t = (10, 3)
t = (4, 3)
t = (-1 << 31, 1)
r = Solution().divide(t[0], t[1])
print(r)
