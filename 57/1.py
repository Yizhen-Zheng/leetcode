from typing import List


class Solution:
    def insertI(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        since they're not overlapping, there won't be [[0,2], [0,4]]
        '''
        if not intervals:
            return [newInterval]
        new_s, new_e = newInterval
        if intervals[-1][-1] < new_s:
            intervals.append(newInterval)
            return intervals
        if intervals[0][0] > new_e:
            # res = [newInterval]
            # res.extend(intervals) # note that extend returns None!!!
            res = [newInterval]+intervals
            return res
        res = []
        idx = 0
        while idx < len(intervals):
            start, end = intervals[idx]
            if end < new_s or start > new_e:
                res.append(intervals[idx])
                if end < new_s and 0 <= idx < len(intervals)-1:
                    if intervals[idx+1][0] > new_e:
                        res.append(newInterval)
                idx += 1
                continue
            merged_s, merged_e = min(start, new_s), max(end, new_e)
            idx += 1
            while idx < len(intervals):
                next_s, next_e = intervals[idx]
                if merged_e < next_s:
                    break
                merged_e = max(merged_e, next_e)
                idx += 1
            res.append([merged_s, merged_e])

        return res

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        binary search:
        find the start idx where i should insert before
            all start that right of this is >= new_s
        find the end idx where i should insert after
            all end that left of this is <= new_e
        to find the rightmost interval that start < new_s:
        [s1----e1]---[]----[s2---e2]]
               ˆ            ˆ
            [new_s--------new_e]
        compare s1, new_s, e2, new_e
        '''
        if not intervals:
            return [newInterval]
        new_s, new_e = newInterval
        if intervals[-1][-1] < new_s:
            intervals.append(newInterval)
            return intervals
        if intervals[0][0] > new_e:
            # res = [newInterval]
            # res.extend(intervals) # note that extend returns None!!!
            res = [newInterval]+intervals
            return res
        res = []
        l, r = 0, len(intervals)-1
        # search end
        while l < r:
            m = (l+r)//2
            end = intervals[m][1]
            if end < new_s:
                l = m+1  # end up some end that end >= new_s
            else:
                r = m
        start_idx = l

        # search start
        l, r = 0, len(intervals)-1
        while l < r:
            m = (l+r+1)//2
            start = intervals[m][0]
            if start > new_e:
                r = m-1
            else:
                l = m  # end up some start that s <= new_e
        end_idx = l
        if intervals[start_idx][0] > new_e:
            # or
            # if intervals[end_idx][1] < new_s:
            # means no overlapping
            '''
     [s2---e2]-------------------------[s1----e1]---[]----[]
      ˆ     †                           †     ˆ
                 [new_s--------new_e]
                                 †
            '''
            return intervals[:start_idx] + [newInterval]+intervals[start_idx:]
        merged_s = min(new_s, intervals[start_idx][0])
        merged_e = max(new_e, intervals[end_idx][1])
        return intervals[:start_idx]+[[merged_s, merged_e]]+intervals[end_idx+1:]


t = [[1, 1]]
n = [0, 0]
t = [[0, 2], [4, 4]]
# t = []
# n = [3, 3]
n = [2, 5]
# n = [5, 5]
# n = [0, 5]
r = Solution().insert(t, n)
print(r)
