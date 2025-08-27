from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        '''
        14:57-15:20 23min not sure if works
        looks like hashmap or linkedlist in array
        pairs are unique
        detect circle in directed graph?
        maybe need trackback, DFS
        naive solution:
        DFS, 
        t: O(n**2) (potentially visit all)
        s: O(E)
        '''
        # total nodes number: numCourses, edges: len(pre)
        adj = defaultdict(list)  # key: course, arr: prerequest(s)
        for s, e in prerequisites:
            adj[s].append(e)

        def dfs(cur: int, visited: list[bool]):
            visited[cur] = True
            has_circle = False
            for neighbor in adj[cur]:
                if visited[neighbor]:
                    return True
                has_circle |= dfs(neighbor, visited)
                if has_circle:
                    return has_circle
            visited[cur] = False
            return has_circle
        for s in range(numCourses):
            has_circle = dfs(s, [False]*numCourses)
            if has_circle:
                return True
        return False

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        '''
        memorization
        15:20-15:29
        debug:-15:33
        13mins
        t: O(n)
        s: O(n)
        '''
        is_circle_start = [None]*numCourses
        visited = [False]*numCourses  # only need a global visited
        adj = defaultdict(list)  # key: course, arr: prerequest(s)
        for s, e in prerequisites:
            adj[s].append(e)

        def dfs(cur: int):
            if is_circle_start[cur] is not None:
                return is_circle_start[cur]
            visited[cur] = True
            has_circle = False
            for neighbor in adj[cur]:
                if visited[neighbor]:
                    has_circle = True
                    break
                has_circle |= dfs(neighbor)
                if has_circle:
                    break
            visited[cur] = False
            is_circle_start[cur] = has_circle
            return has_circle

        for s in range(numCourses):
            if is_circle_start[s] is None:
                is_circle_start[s] = dfs(s)
            if is_circle_start[s] is True:
                return False
        return True

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        '''
        try stack
        '''
        is_circle_start = [None]*numCourses
        visited = [False]*numCourses
        adj = defaultdict(list)  # key: course, arr: prerequest(s)
        for s, e in prerequisites:
            adj[s].append(e)

        for i in range(numCourses):
            if is_circle_start[i] is None:  # cur doesn't have result yet
                s = [(i, False)]
                while s:
                    cur, is_backtrack = s.pop()
                    if is_circle_start[cur] is None:  # cur doesn't have result yet
                        if is_backtrack is False:
                            visited[cur] = True
                            s.append((cur, True))
                            for neighbor in adj[cur]:
                                if visited[neighbor]:  # find circle, return
                                    return False
                                s.append((neighbor, False))
                        else:
                            visited[cur] = False
                            is_circle_start[cur] = False
        return True

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        '''same as above'''
        done = [False]*numCourses
        visited = [False]*numCourses
        adj = defaultdict(list)  # key: course, arr: prerequest(s)
        for s, e in prerequisites:
            adj[s].append(e)

        def dfs(cur: int):
            if done[cur]:
                return True  # has confirmed no circle from cur
            if visited[cur]:
                return False  # circle, cannot finish
            visited[cur] = True
            for neighbor in adj[cur]:
                if dfs(neighbor) is False:
                    return False
            visited[cur] = False
            done[cur] = True
            return True
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        '''
        try queue,BFS
        similar to 310, remove leaf nodes gradually
        this method is called topological sort
        difference from 310:
        this one is directed graph,
        in-degrees(course-to-pre) are different from pre-to-course
        we both need to know how many pre a course has
        and those courses use a specific pre as pre
            (so when we finish a pre, we can retrieve the courses and count down)  
        '''
        # in order to take i, how many pres left need to be taken
        # in degrees( [pre] -> [course]), how many pre
        count_pres = {i: 0 for i in range(numCourses)}
        # key: pre, value: courses use i as prerequest
        adj = {i: []for i in range(numCourses)}
        for course, prer in prerequisites:
            adj[prer].append(course)
            count_pres[course] += 1
        finished_courses = 0
        q = deque()
        for course, pre_count in count_pres.items():
            if pre_count == 0:
                q.append(course)
        while q:
            cur_course = q.popleft()
            finished_courses += 1
            for neighbor in adj[cur_course]:
                count_pres[neighbor] -= 1
                if count_pres[neighbor] == 0:
                    q.append(neighbor)
        if finished_courses == numCourses:
            return True
        return False


t = (2, [[1, 0]])
t = (3, [[0, 2], [1, 2]])
r = Solution().canFinish(t[0], t[1])
print(r)
