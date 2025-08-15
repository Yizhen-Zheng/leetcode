from collections import Counter, defaultdict, deque
import heapq


class Solution:
    '''
    greedy: if nothing available, append idle
    need to know the best choice
    heap? store 'cooling time' of each, 
    strategy?
    '''

    def leastInterval(self, tasks: list[str], n: int) -> int:
        '''
        70min
        brute force: rec, try append each, 
        t: O(m^m), 
        s:O(m^m)
        need to update all tasks' cooling time at every task done:
            maybe look if prev n has that elem(O(n)), n up to 100
            so a cooldown[] is better
        each rec need to:
        update cooldown time,try all possible solution, find that len and return
        '''
        if not tasks or n == 0:
            return len(tasks)

        a = ord('A')
        m = len(tasks)  # all tasks number
        cooldown = [0]*26
        count_task = [0]*26
        for c in tasks:
            idx = ord(c)-a
            count_task[idx] += 1

        def rec(cur_len: int, cooldown: list, count_task: list, remain: int):
            if remain == 0:
                return cur_len

            # first cool down used
            for i in range(26):
                if cooldown[i] > 0:
                    cooldown[i] -= 1

            best_len = float('inf')
            for i in range(26):  # try to find a task next can do
                if count_task[i] > 0 and cooldown[i] == 0:
                    new_count_task = count_task.copy()
                    new_count_task[i] -= 1
                    new_cooldown = cooldown.copy()
                    new_cooldown[i] = n+1
                    path_len = rec(cur_len+1, new_cooldown, new_count_task, remain-1)
                    best_len = min(best_len, path_len)
            if best_len == float('inf'):
                best_len = rec(cur_len+1, cooldown, count_task, remain)
            return best_len
        ans = rec(0, cooldown, count_task, m)
        return ans

    def leastInterval(self, tasks: list[str], n: int) -> int:
        '''
        maybe use (de?)queue + heap
        bfs,shortest path
        '''
        m = len(tasks)  # all tasks number
        count_tasks = defaultdict(int)
        for c in tasks:
            count_tasks[c] += 1
        q = deque([])
        while q:
            c

    def leastInterval(self, tasks: list[str], n: int) -> int:
        '''
        pure counting and Greedy 
        '''
        a = ord('A')
        count_task = [0]*26
        most_frequent_count = 0
        top_frequency = 0
        for c in tasks:
            idx = ord(c)-a
            count_task[idx] += 1
            if count_task[idx] > top_frequency:
                top_frequency = count_task[idx]
                most_frequent_count = 1  # find new top,reset
            elif count_task[idx] == top_frequency:
                most_frequent_count += 1
        # print(top_frequency, most_frequent_count)

        # A A A -> 2 segment
        segment = top_frequency-1
        # AB_AB_AB: n=2, available segment len=1(2-2+1)
        segment_len = n-most_frequent_count+1
        # how many tasks can be inserted inbetween
        empty_slots = segment*segment_len
        # not top frequency tasks number
        remain_tasks = len(tasks)-top_frequency*most_frequent_count
        idles = max(0, empty_slots-remain_tasks)

        ans = len(tasks)+idles
        return ans

    def leastInterval(self, tasks: list[str], n: int) -> int:
        '''
        try remember
        '''
        a = ord('A')
        m = [0]*26
        max_frequency = 0
        max_frequency_count = 0

        for t in tasks:
            i = ord(t)-a
            m[i] += 1
            if m[i] > max_frequency:
                max_frequency = m[i]
                max_frequency_count = 1
            elif m[i] == max_frequency:
                max_frequency_count += 1
        ans = (n+1)*(max_frequency-1)+max_frequency
        return max(ans, len(tasks))


t = (['A', 'A', 'B', 'B'], 2)
# t = (["A", "A", "A", "B", "B", "B"], 2)
# t = (["A", "C", "A", "B", "D", "B"], 1)
r = Solution().leastInterval(t[0], t[1])
print(r)
