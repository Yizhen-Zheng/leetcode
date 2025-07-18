'''
每一个线段都有start和end两个数据项，表示这条线段在X轴上从start位置开始到end位置结束。
给定一批线段，求所有重合区域中最多重合了几个线段，首尾相接的线段不算重合。
例如：线段[1,2]和线段[2.3]不重合。
线段[1,3]和线段[2,3]重合
N<=10^4
0<=s,e<=10^5
'''

'''
basic idea:
sort segments by start
for every segment:
if prev_e <= cur_s: count--
if next_s > cur_e: conut++
so we keep watching 3 things

'''
import sys
import heapq


def main():
    n = int(sys.stdin.readline())
    lines = sys.stdin.read().strip().split('\n')
    arr = [list(map(int, line.split())) for line in lines]
    res = solveI(arr, n)
    res = solveIV(arr, n)
    print(res)
    return


def solveI(nums: list, n: int):
    '''
    there won't be 1 as result(at least 2, or 0)
    what's the mean of 'most':
        |_,_._._,___| |__|,  3
        |_,_|__;_,_;, 2
    most brute-force: n^3, for each segment, count how many overlap it has with others(n-1 elems)

    how about only count segments those have start that comes after current's s?
    (for current, it may be also counted into someone prev's)

    if we can sort them, for every part, only do the calculate the 'parent' which spans longest
    (case 1: 2 parents, case2: ??)
    no matter we decide by new end fall into s and e or new start fall into s and e, 
    results are the same
    '''
    max_count = 0
    nums.sort(key=lambda x: x[0])
    for i in range(n):
        cur_s, cur_e = nums[i]
        count = [1]*(cur_e-cur_s+1)
        for j in range(i+1, n):
            s, e = nums[j]
            if s >= cur_e:
                break
            end = min(cur_e, e)
            if count[s-cur_s] == count[s-cur_s+1]:
                count[s-cur_s] += 1
            for idx in range(s+1, end+1):  # if s==e, it will be skipped
                count[idx-cur_s] += 1
        max_count = max(max_count, max(count))
    return max_count if max_count > 1 else 0


def solveII(nums: list, n: int):
    '''
    reduce duplicated calculation: 
    for every segment, we have many repeated calculation
    if one segment finds a result, some part can be reused by following segment
    then the question is how we detect what parts can be reused, what not?
        to find those goes out of new start at next iteration(no need to handle end)
    '''
    return


def solveIII(nums: list, n: int):
    '''
    do with while loop and 3 ptr(cur, prev, next)
    '''
    nums.sort(key=lambda x: (x[0], x[1]))

    prev, next, cur = 0, 0, 0
    max_count = 0
    count = 0
    while cur < n:
        cur_s, cur_e = nums[cur]
        while next < n and nums[next][0] < cur_e:
            count += 1
            next += 1
        while prev < cur and nums[prev][1] < cur_s:
            count -= 1
            prev += 1
        cur += 1
        max_count = max(max_count, count)
    return max_count if max_count > 1 else 0


def solveIV(nums: list, n: int):
    '''
    heap
    '''
    min_heap = []
    nums.sort(key=lambda x: x[0])
    max_count = 0
    for i in range(n):
        while min_heap and min_heap[0] <= nums[i][0]:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, nums[i][1])
        max_count = max(max_count, len(min_heap))
    return max_count if max_count > 1 else 0


def solveV(nums: list, n: int):
    '''
    map s, e and count(just like count parentheses)
    sort: O(nlogn)
    count: O(nlogn)
        heap up/down: O(logn)
        pop / push operation time for each segment: 1 time
        total pop/push operations: n

    '''
    events = []
    for s, e in nums:
        events.append((s, 1))
        events.append((e, -1))
    events.sort()
    cur_count = 0
    max_count = 0
    for _, delta in events:
        cur_count += delta
        max_count = max(max_count, cur_count)
    return max_count if max_count > 1 else 0


def solveVI(nums: list, n: int):
    '''

    '''


main()
