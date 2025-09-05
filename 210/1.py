from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        '''
        7:53-8:03
        10min
        graph,path
        '''
        ans = []
        count_prer = [0]*numCourses  # count indegrees
        degrees = defaultdict(set)  # adjacent list
        for c, p in prerequisites:
            count_prer[c] += 1
            degrees[p].add(c)
        q = deque()
        for c, p in enumerate(count_prer):
            if p < 1:
                q.append(c)
        while q:
            take = q.popleft()
            ans.append(take)
            for next_c in degrees[take]:
                count_prer[next_c] -= 1
                if count_prer[next_c] < 1:
                    q.append(next_c)
        return ans if len(ans) == numCourses else []

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        '''
        OMG! i misunderstood the adj ! a set doesn't make any sense
        as you're only going to visit a 'available course' once, 
        the adj list of that course will also be used once
        and since it's a DIRECTED GRAPH, an indegree doesn't mean there's an out degree
        '''
        ans = []
        count_prer = [0]*numCourses  # count indegrees
        degrees = [[] for _ in range(numCourses)]  # adjacent list
        for c, p in prerequisites:
            count_prer[c] += 1
            degrees[p].append(c)
        q = deque()
        for c, p in enumerate(count_prer):
            if p < 1:
                q.append(c)
        while q:
            take = q.popleft()
            ans.append(take)
            for next_c in degrees[take]:
                count_prer[next_c] -= 1
                if count_prer[next_c] < 1:
                    q.append(next_c)
        return ans if len(ans) == numCourses else []
