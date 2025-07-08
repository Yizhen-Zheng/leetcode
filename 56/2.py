from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        look at head(arr[0][0]), look at tail(arr[-1][-1]), -> if no need to merge
        begin<=end
        '''
        if len(intervals) <= 1:
            return intervals

        lookup = [0]*(10**4+1)
        duplicated = [False]*(10**4+1)
        merged = []

        for head, tail in intervals:
            if head == tail:
                duplicated[head] = True
                continue
            lookup[head] += 1
            lookup[tail] -= 1
        prev = None
        counter = 0
        for i in range(len(lookup)):
            cur = lookup[i]
            d = duplicated[i]
            if d:
                if not (prev != None or cur != 0):
                    merged.append([i, i])
            if cur > 0:
                if counter == 0:
                    prev = i  # new start
                counter += cur
            elif cur < 0:
                counter += cur
                if counter == 0:
                    merged.append([prev, i])
                    prev = None

        return merged


t = [[0, 5], [1, 1]]
# t = [[1, 2], [0, 2], [0, 6]]
t = [[1, 1], [2, 2], [5, 6]]
r = Solution().merge(t)
print(r)
