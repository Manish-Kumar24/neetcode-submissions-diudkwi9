class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        inf = float('inf')
        adj = [[] for _ in range(n+1)]
        for u, v, w in times:
            adj[u].append((v, w))
        dist = [inf] * (n+1)
        dist[k] = 0
        minHeap = [(0, k)]
        while minHeap:
            d, node = heapq.heappop(minHeap)
            if d > dist[node]:
                continue
            for nbr, wt in adj[node]:
                if d + wt < dist[nbr]:
                    dist[nbr] = d + wt
                    heapq.heappush(minHeap, (dist[nbr], nbr))
        ans = max(dist[1:])
        return ans if ans != inf else -1