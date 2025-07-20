class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        '''
        brute force: O(n), just and all
        '''
        ans = left
        for i in range(left+1, right+1):
            ans &= i
        return ans

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        '''
        find the last SAME bit in left and right?
        O(1)
        how it works: extract all same digits from most significan digit
        e,g,:
        0 1 0 0 1 1
        0 0 1 1 1 1
        res: 0, since they differ from first digit
        0 1 1 0 1 1
        0 1 1 1 1 1
        res: 011000, they differ from 3rd digit, and have first 2 digits the same
        '''
        a, b = left, right
        ans = 0
        count = 0
        while right:
            right >>= 1
            count += 1
        for i in range(count-1, -1, -1):
            operator = 1 << i  # the 2's power to & with l and r
            cur_digit_a = (a & operator) >> i  # extract that digit by shifting to rightmost
            cur_digit_b = (b & operator) >> i
            if cur_digit_b == 1 and cur_digit_a == 0:
                break
            elif cur_digit_a == cur_digit_b == 1:
                ans |= operator

        return ans

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        '''
        a clean version works similar as above
        '''
        count = 0
        while left < right:
            left >>= 1
            right >>= 1
            count += 1
        return left << count


t = [2, 3]
t = [1, 5]
# t = [1, 1]
# t = [64, 500]
t = [64, 70]
r = Solution().rangeBitwiseAnd(t[0], t[1])
print(r)
