class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topoSort(conds):
            adj = defaultdict(list)
            indeg = [0] * (k+1)
            for u, v in conds:
                adj[u].append(v)
                indeg[v] += 1
            q = deque()
            for node in range(1, k+1):
                if indeg[node] == 0:
                    q.append(node)
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for nbr in adj[node]:
                    indeg[nbr] -= 1
                    if indeg[nbr] == 0:
                        q.append(nbr)
            if len(order) != k:
                return []
            return order
        rowOrder = topoSort(rowConditions)
        colOrder = topoSort(colConditions)
        if not rowOrder or not colOrder:
            return []
        rowPos = {}
        for i in range(k):
            rowPos[rowOrder[i]] = i
        colPos = {}
        for i in range(k):
            colPos[colOrder[i]] = i
        matrix = [[0] * k for i in range(k)]
        for num in range(1, k+1):
            r = rowPos[num]
            c = colPos[num]
            matrix[r][c] = num
        return matrix