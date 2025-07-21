class Solution:
    def reverseBitsI(self, n: int) -> int:
        '''
        since n is even, first digit is 0 either direction
        '''
        if not n:
            return 0
        digits = [0]*32
        idx = 0
        while n:
            digits[idx] = n & 1
            n >>= 1
            idx += 1
        print(digits)
        res = 0
        for i in range(idx, 0, -1):
            res |= (digits[i] << (31-i))

        m = res
        visualizer = [0]*32
        midx = 31
        while midx > -1:
            visualizer[midx] = m & 1
            m >>= 1
            midx -= 1
        print(visualizer)
        return res

    def reverseBitsII(self, n: int) -> int:
        '''
        simplier
        '''

        digits = [0]*32
        idx = 0
        nn = n
        while nn:
            digits[idx] = nn & 1
            nn >>= 1
            idx += 1
        print(digits)
        #
        shift_count = 0
        res = 0
        while n:
            cur_digit = (n & 1)
            res |= (cur_digit << (31-shift_count))
            n >>= 1
            shift_count += 1
        #
        m = res
        visualizer = [0]*32
        midx = 31
        while midx > -1:
            visualizer[midx] = m & 1
            m >>= 1
            midx -= 1
        print(visualizer)
        return res

    def reverseBitsIII(self, n: int) -> int:
        '''
        shift together
        '''
        digits = [0]*32
        idx = 0
        nn = n
        while nn:
            digits[idx] = nn & 1
            nn >>= 1
            idx += 1
        print(digits)
        #
        res = 0
        for _ in range(31):  # shift 31 times(up to 2^31)
            res |= (n & 1)
            n >>= 1
            res <<= 1
        #
            m = res
        visualizer = [0]*32
        midx = 31
        while midx > -1:
            visualizer[midx] = m & 1
            m >>= 1
            midx -= 1
        print(visualizer)
        return res

    def reverseBits(self, n: int) -> int:
        '''
        merge change:
        pair swap(1) -> pair swap(2) -> pair swap(4) -> pair swap(8) -> pair swap(16)
        note that first remove intervals, then shift, then merge
        1:
        1111 1111 -> 1010 1010, 0101 0101
         1010 1010 >>1
       0101 0101 <<1
        2:
          1100 1100 >>2
      0011 0011 <<2
        '''
        def visualize(n):
            digits = [0]*32
            idx = 31
            nn = n
            while nn:
                digits[idx] = nn & 1
                nn >>= 1
                idx -= 1
            print(digits)
        n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
        visualize(n)
        n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
        visualize(n)
        n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
        visualize(n)
        n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
        visualize(n)
        # n = (n >> 16) | (n << 16) # python will automatically expand
        n = ((n & 0xFFFF0000) >> 16) | ((n & 0x0000FFFF) << 16)
        visualize(n)
        return n


t = 4
t = 6
# t = 0
t = 43261596
r = Solution().reverseBitsIII(t)
print(r)
r = Solution().reverseBits(t)
print(r)
