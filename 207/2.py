from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        '''
        try union set...?(okey seems not this problem)
        7:55-8:12
        (course,pre)
        BFS and pruning the out-most in a directed graph
        '''
        if numCourses == 1:
            return True
        taken = 0
        can_take = []
        count_p = [0]*numCourses  # count prerequest of course[c]
        p_to_c = defaultdict(set)  # p be a prerequest of courses
        for c, p in prerequisites:
            count_p[c] += 1
            p_to_c[p].add(c)
        for c, p in enumerate(count_p):
            if p == 0:
                can_take.append(c)
        while can_take:
            next_layer = []
            for c in can_take:
                for neighbor in p_to_c[c]:
                    count_p[neighbor] -= 1
                    if count_p[neighbor] == 0:
                        next_layer.append(neighbor)
            taken += len(can_take)
            can_take = next_layer
        return taken == numCourses

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        '''

        '''
