'''
    all other elems appears m times, find the one appears less than m times
    contains negative
    brute force: 
    (sum(set(nums)) * 3 - sum(nums))//2

    a=-2
    b=a&0xFFFFFFFF <-limit a within 32 digits
    print(b)
    4294967294
    print(b-2**32) <- convert back(add sign manually)
-2
'''


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        '''
        approach 1: extend the sum approach in binary:
        for every digit:
            extract the digit from all of the numbers and sum them, take modulo by 3
            if ans has that digit, the digit should be 1 
            if not, the sum is a multiple of 3, so it's 0 on ans's corresponding digit
            add that digit to ans by ans |=digit_res<<i (i is the digit number)
        '''
        m = 3
        ans = 0
        for i in range(32):
            digit_sum = 0
            for n in nums:
                digit_sum += ((n & 0xFFFFFFFF) >> i) & 1
            digit_res = digit_sum % m
            ans |= digit_res << i
        return ans if ans < 2**31 else ans-2**32

    def singleNumber(self, nums: list[int]) -> int:
        '''
        ones: store all bits that appeared exactly once, 
            by &(~twos), exclude those already in twos
        twos: store all bits that appeared exactly twice 
        the third time:
            check with ones: it already in twos, not add in
            go into twos, then the element will be canceled out
        '''
        ones, twos = 0, 0

        for n in nums:
            ones ^= n & (~twos)
            twos ^= n & (~ones)
        return ones


t = [1, 1, 1, 3]
t = [1, 3, 7, 3, 7, 7, 3]
r = Solution().singleNumber(t)
print(r)
