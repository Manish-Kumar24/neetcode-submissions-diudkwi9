class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        q = deque()
        fresh = 0
        time = 0
        # count fresh and push rotten
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        while q and fresh > 0:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for dx, dy in dirs:
                    row = i + dx
                    col = j + dy
                    if (0 <= row < m and 0 <= col < n and grid[row][col] == 1):
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row, col))
            time += 1
        return time if fresh == 0 else -1