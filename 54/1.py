class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        '''
        14:21-14:50
        31min
        t:O(n*m)
        s:O(n*m)
        '''
        m = len(matrix)
        n = len(matrix[0])
        used = [[False]*n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_x, cur_y = 0, 0
        count = 0
        ans = []
        while 0 <= cur_x < m and 0 <= cur_y < n and used[cur_x][cur_y] == False:
            # mark current position used
            ans.append(matrix[cur_x][cur_y])
            used[cur_x][cur_y] = True
            xx, yy = directions[count]  # get direction
            next_x, next_y = cur_x+xx, cur_y+yy
            # detect if should change direction: hit boundary or path
            if not (0 <= next_x < m and 0 <= next_y < n and used[next_x][next_y] == False):
                count = (count+1) % 4  # change direction
                xx, yy = directions[count]
                next_x, next_y = cur_x+xx, cur_y+yy
            cur_x, cur_y = next_x, next_y  # go next
        return ans

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        '''
        simulation like: 
        l to r, r to b, r to l, b to top+1, shrink l,r,b,t
        '''
        m = len(matrix)
        n = len(matrix[0])
        left, right, top, bottom = 0, n-1, 0, m-1  # boundary
        ans = []
        x, y = 0, 0  # cur
        while len(ans) < m*n:
            for x in range(left, right+1):  # can reach right bound
                ans.append(matrix[y][x])
            for y in range(top+1, bottom+1):  # can reach bottom bound
                ans.append(matrix[y][x])
            if top != bottom:
                for x in range(right-1, left-1, -1):  # can reach left bound
                    ans.append(matrix[y][x])
            if left != right:
                for y in range(bottom-1, top, -1):  # can not reach top bound
                    ans.append(matrix[y][x])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return ans


t = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r = Solution().spiralOrder(t)
print(r)
