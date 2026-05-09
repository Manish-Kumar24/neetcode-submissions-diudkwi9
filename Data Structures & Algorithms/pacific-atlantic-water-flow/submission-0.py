class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i, j, visit):
            visit.add((i, j))
            for dx, dy in dirs:
                row = i + dx
                col = j + dy
                if 0<=row<m and 0<=col<n and (row, col) not in visit and heights[row][col]>=heights[i][j]:
                    dfs(row, col, visit)
        for j in range(n):
            dfs(0, j, pacific)
        for i in range(m):
            dfs(i, 0, pacific)
        for j in range(n):
            dfs(m - 1, j, atlantic)
        for i in range(m):
            dfs(i, n - 1, atlantic)
        ans = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    ans.append([i, j])
        return ans