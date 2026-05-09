class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(-1,0), (1, 0), (0, -1), (0, 1)]
        islands = 0
        def dfs(i, j):
            grid[i][j] = '0'
            for dx, dy in dirs:
                row = i + dx
                col = j + dy
                if 0 <= row < m and 0 <= col < n and grid[row][col] == '1':
                    dfs(row, col)
            return
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        return islands