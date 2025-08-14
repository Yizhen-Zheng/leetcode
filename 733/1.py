from typing import List
from collections import deque


class Solution:
    '''
    no need to backtrace
    just dfs, as visited is modified different from origin color
    and handle when origin == target before dfs. (in that case, return origin img)
    e,g, source=[0,1],color=1
        [[0,1,1]
        ,[0,0,0,]], origin cell can be visited twice and creat infinit loop
        this case nothing to modify
         [[0,1,0]
        ,[0,0,0,]], ok but no need to traverse(so nothing to modify)
    '''

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
        graph traverse
        13:36-13:47
        11min
        BFS
        t:O(n*m)
        s:O(n*m)
        '''
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(image), len(image[0])
        origin_color = image[sr][sc]
        q = deque([(sr, sc)])
        s = set()
        while q:
            r, c = q.popleft()
            image[r][c] = color
            for rr, cc in directions:
                nr, nc = r+rr, c+cc
                if -1 < nr < m and -1 < nc < n and (nr, nc) not in s:
                    if image[nr][nc] == origin_color:
                        q.append((nr, nc))
                        s.add((nr, nc))
        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
        7min
        DFS
        back-trace, not using set
        t:O(n*m)
        s:O(n*m)
        '''
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(image), len(image[0])
        origin_color = image[sr][sc]

        def dfs(image, r, c):
            image[r][c] = '#'
            for rr, cc in directions:
                nr, nc = r+rr, c+cc
                if -1 < nr < m and -1 < nc < n:
                    if image[nr][nc] == origin_color:
                        dfs(image, nr, nc)
            image[r][c] = color
            return
        dfs(image, sr, sc)
        return image
