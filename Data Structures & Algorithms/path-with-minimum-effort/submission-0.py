class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        minHeap = [(0, 0, 0)]    # effort, r, c
        while minHeap:
            effort, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == m-1 and c == n-1:
                return effort
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0<=nr<m and 0<=nc<n and (nr, nc) not in visited:
                    diff = abs(heights[r][c] - heights[nr][nc])
                    newEffort = max(diff, effort)
                    heapq.heappush(minHeap, (newEffort, nr, nc))