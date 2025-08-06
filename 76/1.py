from collections import Counter, deque, defaultdict


class Solution:
    def minWindowI(self, s: str, t: str) -> str:
        '''
        8:55-9:06
        9:33-10:00
        bture force:  40min, work, TLE
            enum all substr that contains s
            bfs
            t:(2^n)
            s:(2^n)
        'a', 'aa' is false, that means need to mark 'used'
        cannot use set(duplication in t)
        idea:
        graph(seems close to O(n+m)),dp,divide and conquer
        ans is unique

        try sliding window
        count all, try reduce or add and see if satisfy? 
        '''
        m = len(s)
        n = len(t)

        def compare(s):  # O(m+2n)
            s_dict = defaultdict(int, Counter(s))  # O(m)
            t_dict = dict(Counter(t))  # O(n)
            for key in t_dict.keys():  # O(n)
                if s_dict[key] < t_dict[key]:
                    return False
            return True
        if not compare(s):
            return ''
        q = deque([(0, m-1)])
        seen = set()  # O(2^n)
        min_l, min_r = 0, m-1
        while q:  # perms: 2^n
            l, r = q.popleft()
            if min_r-min_l > r-l:
                min_l, min_r = l, r
            for new_l, new_r in [(l+1, r), (l, r-1)]:
                new_s = s[new_l:new_r+1]
                if new_s not in seen:
                    seen.add(new_s)
                    if compare(new_s):
                        q.append((new_l, new_r))
        return s[min_l:min_r+1]

    def minWindow(self, s: str, t: str) -> str:
        '''
        not work(infinit loop)
        10:00-10:52-11:57
        BFS(?)
        each path needs to keep watch cur_min and cur_max
        maintain individual used
        q: current node, used, current left most used, current right most used
        once reached to t[n-1], return immediately
        not work but why?
        t: ?
        s:?
        purge
        visit l-most and r-most first to be more efficient?
        once get one ans, purge immediately
        '''
        m = len(s)
        n = len(t)
        s_dict = defaultdict(list)  # acsending order
        for i in range(m):  # O(m)
            s_dict[s[i]].append(i)
        used = [False]*m
        q = deque([(-1, used, m, -1)])
        cur_node_idx = -1
        max_l, min_r = 0, m-1
        finished = False
        while q:
            cur_node_idx, cur_used, l_most, r_most = q.pop()
            if cur_node_idx == n-1:
                finished = True
                if r_most-l_most < min_r-max_l:  # update record
                    max_l, min_r = l_most, r_most
                continue
            next_node = t[cur_node_idx+1]
            # iterate from side(0, num-1) to center
            for next_pos_idx in range((len(s_dict[next_node])-1)//2+1):  # O(m)
                l_next, r_next = next_pos_idx, len(s_dict[next_node])-next_pos_idx-1
                for next_pos_idx_side in ([l_next, r_next]):
                    next_pos = s_dict[next_node][next_pos_idx_side]
                    if not cur_used[next_pos]:
                        next_used = cur_used.copy()
                        next_used[next_pos] = True
                        next_l_most = min(l_most, next_pos)
                        next_r_most = max(r_most, next_pos)
                        if next_r_most-next_l_most <= min_r-max_l:  # can improve
                            q.append((cur_node_idx+1, next_used, next_l_most, next_r_most))
        return s[max_l:min_r+1] if finished else ''

    def minWindow(self, s: str, t: str) -> str:
        '''
        t:O(m+n)
        s:O(1)(up to 52 chars)
        '''
        m = len(s)
        n = len(t)
        s_dict = defaultdict(int, Counter(s))  # acsending order
        todo = dict(Counter(t))  # O(n), count occurence
        remain = n
        for key in todo.keys():  # O(n), check valid
            if s_dict[key] < todo[key]:
                return ''
        l, r = 0, 0
        best_l, best_r = 0, m-1
        while r < m:  # O(n+m)
            tail_added = s[r]
            if todo.get(tail_added, -1) > 0:
                remain -= 1
            if tail_added in todo:
                todo[tail_added] -= 1
            while remain == 0:
                if (r - l) < (best_r - best_l):
                    best_r, best_l = r, l
                head_to_throw = s[l]
                if todo.get(head_to_throw, -1) == 0:
                    remain += 1
                if head_to_throw in todo:
                    todo[head_to_throw] += 1
                l += 1
            r += 1
        return s[best_l:best_r+1]

    def minWindow(self, s: str, t: str) -> str:
        '''
        follow tutorial
        grabage char will have negative value, and won't effect res
        once garbage becomes 0, it goes out of window
        '''
        m, n = len(s), len(t)
        l, r = 0, 0
        todo = [0]*123
        remain = n
        for c in t:
            todo[ord(c)] += 1
        best_l, best_r = 0, m
        while r < m:
            to_add = s[r]
            if todo[ord(to_add)] > 0:
                remain -= 1
            todo[ord(to_add)] -= 1
            while remain == 0:
                if r-l < best_r-best_l:  # update best
                    best_r, best_l = r, l
                to_remove = s[l]
                if todo[ord(to_remove)] == 0:
                    remain += 1
                todo[ord(to_remove)] += 1
                l += 1
            r += 1
        return s[best_l:best_r+1] if best_r != m else ''


t = ('abc', 'bc')
t = ('cb', 'cc')
t = ("ADOBECODEBANC", 'ABC')
# t = ("caccaacaaaabbcaccaccc", "acccacbccc")
# t = ("bccbacaaababaabcbabbbbabbcca", "caccabbabcacbabcb")
# t = ("caccaacaaaabbcaccaccc", "acacbc")
r = Solution().minWindowI(t[0], t[1])
print(r)
r = Solution().minWindow(t[0], t[1])
print(r)
