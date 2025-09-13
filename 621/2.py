from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        '''
        math
        8:01-8:17
        t: O(n * 26)(up to 26 kinds of tasks in counter)
        s: O(n)(for counter)
        '''
        if n == 0:
            return len(tasks)
        total = len(tasks)
        c = Counter(tasks)
        top_frequency = 0
        count_top_frequency = 0
        for f in c.values():
            if f > top_frequency:
                top_frequency = f
                count_top_frequency = 1
            elif f == top_frequency:
                count_top_frequency += 1
        idle = (top_frequency-1)*(n-count_top_frequency+1)
        base = top_frequency*count_top_frequency
        remain = max(0, total-base-idle)
        return base+idle+remain

    def leastInterval(self, tasks: list[str], n: int) -> int:
        '''
        deq + heap
        simulate the real process
        the max heap ensures cooldown always execute the most frequent task first
        t:O(n*logn)(the heapq)
        s:O(n)
        '''
        freq = Counter(tasks)
        heap = []
        cooldown = deque()
        timer = 0
        for _, v in freq.items():
            heapq.heappush(heap, -v)

        while heap or cooldown:
            if heap:  # available tasks
                task = -heapq.heappop(heap)
                if task > 1:
                    cooldown.append((task-1, timer+n+1))  # then the task can be de-freeze
            timer += 1  # no matter if there're available tasks, increment timer
            while cooldown and cooldown[0][1] == timer:  # if there are any tasks out of cooldown
                task_count, _ = cooldown.popleft()
                heapq.heappush(heap, -task_count)  # add to available tasks
        return timer


t = (["A", "A", "A", "B", "B", "B"], 2)
r = Solution().leastInterval(t[0], t[1])
print(r)
