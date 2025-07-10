import math
import collections


class Solution:
    def countPrimes(self, n: int) -> int:
        '''

        '''
        if n < 2:
            return 0
        arr = [True]*(n)
        arr[0] = arr[1] = False
        for i in range(math.floor(math.sqrt(n))+1):
            if arr[i] == True:
                start = i*i
                while start < n:
                    arr[start] = False
                    start += i
        count = collections.Counter(arr)
        print(arr)
        return count.get(True)


t = 10
r = Solution().countPrimes(t)
print(r)
