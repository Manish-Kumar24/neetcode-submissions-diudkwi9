class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        n = len(points)
        totalCost = 0
        minHeap =[(0, 0)]
        while len(visited) < n:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            totalCost += cost
            x1, y1 = points[node]
            for nbr in range(n):
                if nbr not in visited:
                    x2, y2 = points[nbr]
                    dist = abs(y2-y1) + abs(x2-x1)
                    heapq.heappush(minHeap, (dist, nbr))
        return totalCost