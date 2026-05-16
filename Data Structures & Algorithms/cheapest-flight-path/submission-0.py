class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # build graph
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))
        inf = float('inf')
        dist = [inf] * n
        dist[src] = 0
        q = deque([(src, 0)])                 # node, 0
        # BFS
        steps = 0
        while q and steps <= k:
            size = len(q)
            tempDist = dist[:]
            for i in range(size):
                node, cost = q.popleft()
                for nbr, price in adj[node]:
                    newCost = cost + price
                    if newCost < tempDist[nbr]:
                        tempDist[nbr] = newCost
                        q.append((nbr, newCost))
            dist = tempDist
            steps += 1
        return dist[dst] if dist[dst] != inf else -1