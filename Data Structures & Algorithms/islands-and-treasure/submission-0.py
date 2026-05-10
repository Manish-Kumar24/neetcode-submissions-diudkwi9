class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        inf = 2147483647
        q = deque()
        # puch 0 into q
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
        # traverse and push back into queue
        while q:
            i, j = q.popleft()
            for dx, dy in dirs:
                row = i + dx
                col = j + dy
                if 0<=row<m and 0<=col<n and grid[row][col] == inf:
                    grid[row][col] = grid[i][j] + 1
                    q.append((row, col))