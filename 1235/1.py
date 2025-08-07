import heapq
import bisect
from collections import defaultdict


class Solution:

    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        '''
        8:14-8:38, 9:14-10:06-75min

        interval ?
        first find how many 'layers' then loop those layer to find max
        O(n*m)
        ???maybe use a ll like structrue, don't pop heap, 
        since one block has multiple choices for what comes after
        need some way to push back
        '''

        all_jobs = []
        n = len(startTime)
        for i in range(n):
            all_jobs.append((startTime[i], endTime[i], profit[i]))
        all_jobs.sort(key=lambda x: x[0])
        no_overlap = defaultdict(int)
        max_p = 0
        heap = []
        idx = 0
        # cur layer>=len?append new:arr[layer]+=profit
        while idx < n:
            s, e, p = all_jobs[idx]
            can_connect = 0
            while heap and can_connect < len(heap):  # ?
                e
                # ?
            heapq.heappush(heap, (e, idx))  # min heap?
            no_overlap[len(heap)-1] += p
            max_p = max(max_p, no_overlap[len(heap)-1])
            idx += 1
        print(no_overlap)
        return max_p

    def jobSchedulingHeap(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        '''
        use a heap, only rec on those adj to head
        s strictly < e
        seems heap not work
        -11:47
        '''
        # jobs = [(0, 0, 0)]  # dummy head
        jobs = []
        for i in range(len(startTime)):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x: x[0])
        n = len(jobs)
        line = [(0, 0)]  # min heap,(e,p)
        for i in range(n):
            s, e, p = jobs[i]
            # if it's nothing prev can connect, push itself
            # overlap with existing min
            if line[0][0] > s:
                heapq.heappush(line, (e, p))
            while line[0][0] <= s:  # can connect
                origin_e, origin_p = line[0]
                heapq.heappush(line, (e, origin_p+p))  # add new
            heapq.heappop(line)  # remove origin head

    def jobSchedulingB(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        '''
        try brute force rec, TLE
        t:O(n^n)
        s:O(n)
        10:15-11:05, 50min
        '''
        jobs = [(0, 0, 0)]
        for i in range(len(startTime)):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x: x[0])
        n = len(jobs)

        def rec(idx, acc):
            cur_p = acc+jobs[idx][2]
            max_p = cur_p
            cur_e = jobs[idx][1]
            todo = []  # minheap, (e,idx_todo)
            # find next adj to visit
            next_idx = idx+1
            while next_idx < n and (len(todo) == 0 or jobs[next_idx][0] < todo[0][0]):
                if jobs[next_idx][0] >= cur_e:  # next s not overlap with exist
                    heapq.heappush(todo, (jobs[next_idx][1], next_idx))
                next_idx += 1
            for _, i in todo:
                next_p = rec(i, cur_p)
                max_p = max(max_p, next_p)
            return max_p
        return rec(0, 0)

    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        '''
        above contains dup calculating
        '''
        jobs = [(0, 0, 0)]
        for i in range(len(startTime)):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x: x[0])
        n = len(jobs)
        memo = [0]*n

        def rec(idx, memo):
            if memo[idx]:
                return memo[idx]
            cur_p = jobs[idx][2]
            max_p = 0
            cur_e = jobs[idx][1]
            todo = []  # minheap, (e,idx_todo)
            # find next adj to visit
            next_idx = idx+1
            while next_idx < n and (len(todo) == 0 or jobs[next_idx][0] < todo[0][0]):
                if jobs[next_idx][0] >= cur_e:  # next s not overlap with exist
                    heapq.heappush(todo, (jobs[next_idx][1], next_idx))
                next_idx += 1
            for _, i in todo:
                next_p = rec(i, memo)
                max_p = max(max_p, next_p)
            memo[idx] = max_p+cur_p
            return memo[idx]
        res = rec(0,  memo)
        print(memo)
        print(max(memo))
        return res

    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        '''
        solution, TLE, memorization
        '''
        jobs = []
        for i in range(len(startTime)):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x: x[0])
        n = len(startTime)
        dp = {}

        def rec(idx, dp):
            if idx == n:
                return 0
            if idx in dp:
                return dp[idx]
            next = n  # find next
            for i in range(idx+1, n):
                if jobs[i][0] >= jobs[idx][1]:
                    next = i
                    break
            include_cur = jobs[idx][2]+rec(next, dp)
            exclude_cur = rec(idx+1, dp)
            dp[idx] = max(include_cur, exclude_cur)
            return dp[idx]
        res = rec(0, dp)
        print(dp)
        return res

    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        '''
        solution,  
        '''
        jobs = []
        for i in range(len(startTime)):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x: x[1])
        n = len(startTime)
        dp = [[0, 0]]

        for s, e, p in jobs:
            i = bisect.bisect(dp, [s+1])-1
            if dp[i][1]+p > dp[-1][1]:
                dp.append([e, dp[i][1]+p])
        print(dp)
        return dp[-1][1]

    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        '''
        solution
        sort by start, search smallest start in [cur_e,n-1]

        '''
        n = len(startTime)
        jobs = []
        for i in range(len(startTime)):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x: x[0])

        def find_next(idx):
            for next_i in range(idx+1, n):
                if jobs[next_i][0] >= jobs[idx][1]:  # start after cur ends
                    return next_i
            return -1
        dp = [0]*n
        dp[-1] = jobs[-1][2]
        for i in range(n-2, -1, -1):
            next_idx = find_next(i)
            add_p = dp[next_idx] if next_idx != -1 else 0
            include = jobs[i][2]+add_p
            dp[i] = max(dp[i+1], include)
        print(dp)
        return dp[0]

    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        '''
        solution
        sort by end, search biggiest end in [0,cur_s]
        '''
        # jobs = []
        jobs = [(0, 0, 0)]
        for i in range(len(startTime)):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x: x[1])
        n = len(jobs)
        dp = [0]*n

        def search(cur):
            l, r = 0, n-1
            s = jobs[cur][0]  # find e<=s
            while l < r:
                m = (l+r)//2
                if jobs[m][1] <= s:
                    l = m+1
                else:
                    r = m
            return l-1
        for i in range(1, n):
            prev_i = search(i)
            include_cur = jobs[i][2] + dp[prev_i]
            exclude_cur = dp[i-1]
            dp[i] = max(include_cur, exclude_cur)
        return dp[-1]

    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        '''
        solution
        sort by start, search smallest s in [cur_e,n-1]
        '''
        # jobs = []
        jobs = []
        for i in range(len(startTime)):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key=lambda x: x[0])
        n = len(jobs)
        dp = [0]*n
        dp[-1] = jobs[-1][2]  # last s has nothing to connect

        def search(cur):
            l, r = 0, n-1
            e = jobs[cur][1]  # find s >= e
            while l < r:
                m = (l+r)//2
                if jobs[m][0] < e:
                    l = m+1
                else:
                    r = m
            return l if jobs[l][0] >= e else -1
        for i in range(n-2, -1, -1):
            last_i = search(i)
            print(last_i)
            include_cur = jobs[i][2] + (dp[last_i] if last_i != -1 else 0)
            exclude_cur = dp[i+1]
            dp[i] = max(include_cur, exclude_cur)
        print(dp)
        return dp[0]


# t = ([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70])
t = ([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60])

r = Solution().jobScheduling(t[0], t[1], t[2])
print(r)

# a = [631, 919, 696, 968, 618, 133, 263, 517, 265, 290, 741, 646, 534, 605, 978, 584, 937, 37, 666, 446, 264, 58, 461, 648, 382, 783, 719, 958, 247, 837, 547, 978, 169, 172, 545, 326, 720, 232, 121, 335, 575, 496, 701, 662, 201, 641, 158, 976, 658, 888,
#      645, 338, 401, 627, 803, 716, 139, 243, 382, 592, 287, 743, 683, 162, 220, 871, 957, 694, 108, 318, 390, 416, 855, 922, 293, 116, 574, 759, 50, 690, 314, 424, 607, 894, 520, 972, 85, 214, 118, 992, 197, 865, 826, 160, 19, 583, 520, 585, 268, 872]
# b = [811, 960, 887, 986, 685, 440, 339, 709, 682, 510, 897, 896, 588, 906, 980, 604, 984, 676, 788, 748, 814, 207, 852, 905, 478, 880, 732, 986, 327, 864, 739, 990, 221, 354, 594, 763, 962, 273, 139, 416, 852, 887, 809, 959, 718, 919, 175, 994, 897, 987,
#      651, 530, 939, 819, 807, 874, 956, 651, 809, 952, 442, 861, 990, 535, 732, 926, 965, 900, 195, 595, 492, 432, 950, 963, 857, 280, 712, 794, 751, 732, 754, 531, 710, 958, 694, 982, 884, 352, 729, 996, 253, 947, 940, 268, 442, 763, 963, 862, 760, 884]
# c = [7, 25, 35, 83, 75, 89, 61, 23, 28, 97, 43, 100, 92, 29, 97, 44, 52, 55, 91, 18, 27, 7, 34, 41, 11, 12, 20, 89, 50, 96, 80, 36, 90, 79, 91, 18, 12, 50, 95, 32, 78, 66, 17, 59, 60, 39, 18, 75, 73,
#      75, 60, 49, 75, 86, 67, 10, 76, 6, 40, 81, 35, 93, 29, 96, 94, 92, 99, 3, 76, 88, 97, 64, 79, 39, 5, 81, 46, 82, 82, 86, 43, 54, 36, 35, 90, 26, 65, 59, 22, 44, 84, 14, 97, 99, 81, 35, 41, 15, 82, 30]
# r = Solution().jobSchedulingB(a, b, c)
# print(r)

# r = Solution().jobScheduling(a, b, c)
# print(r)
