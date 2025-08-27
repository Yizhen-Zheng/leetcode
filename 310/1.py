from collections import defaultdict
from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        '''
        16:15-16:41 26min
        find all possible MHT, return its label
        in other words, find min len in a graph

        brute force: 
        try to bfs with set from every nodes, record len
        t: O(N**2)
        s: O(N)
        TLE
        '''
        graph = defaultdict(list)
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        h_record = [0]*n  # max h when use idx as root
        min_h = n  # record global minimum so far
        for root in range(n):  # try all nodes
            visited = [False]*n
            visited[root] = True  # mark visited
            q = deque([(root, 0)])
            while q:
                cur, cur_h = q.popleft()
                h_record[root] = max(h_record[root], cur_h)
                for neighbor in graph[cur]:
                    if not visited[neighbor]:
                        q.append((neighbor, cur_h+1))
                        visited[neighbor] = True
                        # update min_h if find smaller
            min_h = min(h_record[root], min_h)
        # retrieve ans
        ans = []
        for i in range(n):
            if h_record[i] == min_h:
                ans.append(i)
        print(graph)
        return ans

    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        '''
        seems dp, cuz root a to b is calculated multiple times
        memoriation
        seems no need for visited, cuz n-1 edges, you won't visit a node twice(?)
        9:32 - 9:50, TLE
        '''
        graph = defaultdict(list)
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        h_record = [0]*n  # max h when use idx as root
        min_h = n  # record global minimum so far
        memo = [[-1]*n for _ in range(n)]  # row: start at, col: end at
        for root in range(n):  # try all nodes
            memo[root][root] = 0
            q = deque([(root, 0)])
            while q:
                cur, cur_h = q.popleft()
                memo[root][cur] = cur_h
                h_record[root] = max(h_record[root], cur_h)
                for neighbor in graph[cur]:
                    if memo[root][neighbor] == -1:
                        q.append((neighbor, cur_h+1))
                        # update min_h if find smaller
            min_h = min(h_record[root], min_h)
        # retrieve ans
        ans = []
        for i in range(n):
            if h_record[i] == min_h:
                ans.append(i)
        print(graph)
        print(memo)
        return ans

    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        '''

        '''
        if n == 1:  # one node, no edge
            return [0]
        graph = [set() for _ in range(n)]
        # set for O(1) delete node
        for s, e in edges:
            graph[s].add(e)
            graph[e].add(s)
        print(graph)
        visited = [False]*n
        leaves = []  # sotre node lable
        # leaves: proofed leaves[elem] only have one edge
        for node, edge_set in enumerate(graph):
            if len(edge_set) == 1:
                leaves.append(node)
                visited[node] = True
        prev = []
        while leaves:
            next_leaves = []  # simulate dequeue
            for leaf_label in leaves:
                if len(graph[leaf_label]) > 0:
                    next_leaf_label = graph[leaf_label].pop()  # pop the only neighbor
                    graph[next_leaf_label].remove(leaf_label)  # remove current
                    if len(graph[next_leaf_label]) == 1 and visited[next_leaf_label] == False:
                        next_leaves.append(next_leaf_label)
                        visited[next_leaf_label] == True
            prev = leaves
            leaves = next_leaves
        return prev

    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        '''
        try review above
        t: O(n)(visit each node only once)
        s:O(n)(store leaves, graph)
        '''
        if n == 1:
            return [0]
        graph = [set() for _ in range(n)]
        for s, e in edges:
            graph[s].add(e)
            graph[e].add(s)
        leaves = []  # nodes who only have one neighbor
        for node, neighbors in enumerate(graph):
            if len(neighbors) == 1:
                leaves.append(node)
        remain = n
        while remain > 2:
            remain -= len(leaves)
            next_leaves = []
            for node in leaves:
                neighbor = graph[node].pop()
                # adjust neighbor, and prevent duplicated accessing
                # like burn the bridge back
                graph[neighbor].remove(node)
                if len(graph[neighbor]) == 1:
                    next_leaves.append(neighbor)
            leaves = next_leaves
        return leaves

    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        '''
        longest path
        a mid point must be: the middle of any longest path cross the tree
        like connecting the diagonals of a rectangle, we'll get the 'center'
        or the cross 2 diameters, we find the center has shortest len to reach 4 ends of that diameter
        'longest possible path between any 2 nodes in the tree

        t: O(N)
        s: O(N)
        find mid of arr:
        n=len
        [(n-1)//2:n//2+1]
        '''

        graph = defaultdict(set)
        for s, e in edges:
            graph[s].add(e)
            graph[e].add(s)

        def maxpath(cur, visited: list[int]):
            visited[cur] = True
            longest_path = []
            for neighbor in graph[cur]:
                # it's ok if neighbor[A] removed from visited,
                # as we're going to visit neighbor[B], and as a tree B don't connect A
                # if it's a circulate graph, it's also ok, cuz the 2 paths are different
                # time complexity of this is O(E), we're try each path once
                # and figure out which is longest by comparing
                if not visited[neighbor]:
                    new_path = maxpath(neighbor, visited)
                    if len(new_path) > len(longest_path):
                        longest_path = new_path
            longest_path.append(cur)
            visited[cur] = False  # trackback
            return longest_path

        longest_path = maxpath(0, [False]*n)
        longest_path = maxpath(longest_path[0], [False]*n)
        m = len(longest_path)
        root = longest_path[(m-1)//2:m//2+1]
        return root

    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        '''
        tree dp / reroot
        height1[i]: longest path from i, goes down to i's subtree
        t: O(n)
        s: O(n)
        why use 2: when start traversal, we don't know if start is on the end of longest path
        '''
        adj = defaultdict(set)
        for s, e in edges:
            adj[s].add(e)
            adj[e].add(s)
        height1 = [-1] * n  # h1: go down to i's longest subtree
        height2 = [-1] * n  # h2: from i, go other child's subtree(not the longest child)
        dp = [-1]*n  # h of tree if i is root

        # post order, result generated from leaves to root
        def dfs1(cur, parent):
            h1, h2 = -1, -1  # highest, second highest
            for child in adj[cur]:
                if child == parent:  # prevent duplication in undirected adj
                    continue
                dfs1(child, cur)
                h_use_child_as_subtree = height1[child]+1
                # update primary,secondary highest
                if h_use_child_as_subtree > h1:
                    h2 = h1
                    h1 = h_use_child_as_subtree
                elif h_use_child_as_subtree > h2:
                    h2 = h_use_child_as_subtree
            height1[cur] = max(0, h1)
            height2[cur] = max(0, h2)

        # pre_order
        # calculate dp[cur], means tree height when use cur as root
        def dfs2(cur, parent, acc):
            # longest path: len_above_cur vs len_below_cur
            dp[cur] = max(height1[cur], acc)
            for child in adj[cur]:
                if child == parent:
                    continue
                # calculate acc for child. acc: longest path 'above' child
                path_up_via_cur = acc+1
                # calculate path_down_via_cur_other_child
                if height1[child]+1 == height1[cur]:
                    # child is the longest subtree, choose another child
                    # second longest path down from u
                    path_down_via_cur_other_child = height2[cur]+1
                    # NOTE if cur only has 1 child, [0] - [1],
                    # the path_down_via_cur_other_child is also correctly calculated
                else:
                    # longest path down from cur(choose the longest subtree)
                    path_down_via_cur_other_child = height1[cur]+1
                new_acc = max(path_up_via_cur, path_down_via_cur_other_child)
                dfs2(child, cur, new_acc)
        dfs1(0, -1)
        dfs2(0, -1, 0)
        min_height = min(dp)
        return [i for i, h in enumerate(dp)if h == min_height]


t = (4, [[1, 0], [1, 2], [1, 3]])
r = Solution().findMinHeightTrees(t[0], t[1])
print(r)
