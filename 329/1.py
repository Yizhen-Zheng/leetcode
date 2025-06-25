class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        '''
        at least 1
        time complexity: O(m*n)
        space complexity: O(m*n)
        '''
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        maximum = 0

        def rec(i, j):
            if dp[i][j]:
                return dp[i][j]
            greater_neighbor = []
            for vtc, hrz in directions:
                next_i = i+vtc
                next_j = j+hrz
                if 0 <= next_i < m and 0 <= next_j < n:
                    # if they're in range
                    neighbor_val = matrix[next_i][next_j]
                    current_val = matrix[i][j]
                    if neighbor_val > current_val:
                        greater_neighbor.append((next_i, next_j))
            current_path_len = 0
            for neighbor_i, neighbor_j in greater_neighbor:
                neighbor_path_len = rec(neighbor_i, neighbor_j)
                current_path_len = max(current_path_len, neighbor_path_len)
            dp[i][j] = current_path_len+1
            return current_path_len+1

        for i in range(m):
            for j in range(n):
                path_len = rec(i, j)
                maximum = max(path_len, maximum)
        [print(l)for l in dp]
        return maximum


t = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
t = [[1]]
t = [[1, 3, 5]]
r = Solution().longestIncreasingPath(t)
print(r)
