from typing import List
import heapq


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        '''
        time: O(nlogn)
        space: O(n)
        '''
        intervals.sort(key=lambda x: x[0])
        intersects = []
        group_count = 0
        for s, e in intervals:
            while intersects and intersects[0] < s:
                heapq.heappop(intersects)
            heapq.heappush(intersects, e)
            group_count = max(group_count, len(intersects))
        return group_count

    def minGroupsII(self, intervals: List[List[int]]) -> int:
        '''
        time: O(nlogn)
        space: O(n)
        events: we want to seperare those starts connects end, so append end+1
        [[1,2],[2,3]], should mapped into :[0, 1, 1, -1, -1]
            with the offset one, when one s and one e meet at same position,
            we should first count e(-1), then add s. since the e should end earlier instead of duplicate with this s
            ([[1,2],[3,4]] => mapped as [0,1,0,-1+1,4], instead of 1-1 on idx[3] 
             [[1,2],[2,3]] => mapped as [0,1,1,-1,-1]
            )
        '''
        all_intervals = []
        for s, e in intervals:
            all_intervals.append((s, 1))
            all_intervals.append((e+1, -1))
        all_intervals.sort()
        group_count = 0
        cur_count = 0
        for pos, val in all_intervals:
            cur_count += val
            group_count = max(group_count, cur_count)
        return group_count

    def minGroupsIII(self, intervals: List[List[int]]) -> int:
        '''
        time: O(nlogn)
        space: O(n)
        events: we want to seperare those starts connects end, so append end+1
        [[1,2],[2,3]], should mapped into :[0, 1, 1, -1, -1]
            with the offset one, when one s and one e meet at same position,
            we should first count e(-1), then add s. since the e should end earlier instead of duplicate with this s
            ([[1,2],[3,4]] => mapped as [0,1,0,-1+1,4], instead of 1-1 on idx[3] 
             [[1,2],[2,3]] => mapped as [0,1,1,-1,-1]
            )
        '''
        mapped = [0]*1000002
        for s, e in intervals:
            mapped[s] += 1
            mapped[e+1] -= 1

        group_count = 0
        cur_count = 0
        for delta in mapped:
            cur_count += delta
            group_count = max(group_count, cur_count)
        return group_count

    def minGroupsIV(self, intervals: List[List[int]]) -> int:
        '''
        the mechanism is the same as plotting all s and e on a axi
        |____________________________________|
        s1   s2      e2     s3        e1    e3
        need 2 groups
        s2: starts before the earliest end, means it must overlap
        so we DON'T move end ptr, since next s can also starts before e2
        and to to verify next start
        if next passed current end, means we can put it into existing group(e2's)
        and also means all following s have passed e2, so we don't need e2 anymore
        this is similar to the heap, where we only ask if one interval has any overlapping BEFORE itself,
        by checking numbers of prev e > cur s
        and ignore anything after it(that will be handled by other intervals latter)
        '''
        starts = sorted([x[0] for x in intervals])
        ends = sorted([x[1] for x in intervals])
        cur_e = 0
        count = 0
        for s in starts:
            if s > ends[cur_e]:
                cur_e += 1
            else:
                count += 1
        return count


t = [[0, 0]]
t = [[1, 1], [1, 2]]
# t = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
# r = Solution().minGroups(t)
r = Solution().minGroupsIV(t)
print(r)
