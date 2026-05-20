class DSU:

    def __init__(self, n):

        self.parent = [i for i in range(n)]

        self.rank = [1] * n

    def find(self, x):

        if self.parent[x] != x:

            self.parent[x] = self.find(
                self.parent[x]
            )

        return self.parent[x]

    def union(self, x, y):

        px = self.find(x)

        py = self.find(y)

        # already connected
        if px == py:
            return False

        # union by rank
        if self.rank[px] > self.rank[py]:

            self.parent[py] = px

            self.rank[px] += self.rank[py]

        else:

            self.parent[px] = py

            self.rank[py] += self.rank[px]

        return True


class Solution:

    def findCriticalAndPseudoCriticalEdges(
        self,
        n: int,
        edges: List[List[int]]
    ) -> List[List[int]]:

        # add original index
        newEdges = []

        for i, (u, v, w) in enumerate(edges):

            newEdges.append(
                [w, u, v, i]
            )

        # sort by weight
        newEdges.sort()

        # Kruskal function
        def kruskal(skipEdge, forceEdge):

            dsu = DSU(n)

            cost = 0

            edgesUsed = 0

            # force include edge first
            if forceEdge != -1:

                w, u, v, idx = newEdges[forceEdge]

                if dsu.union(u, v):

                    cost += w

                    edgesUsed += 1

            # normal Kruskal
            for i in range(len(newEdges)):

                # skip edge
                if i == skipEdge:
                    continue

                w, u, v, idx = newEdges[i]

                if dsu.union(u, v):

                    cost += w

                    edgesUsed += 1

            # disconnected graph
            if edgesUsed != n - 1:
                return float('inf')

            return cost

        # original MST cost
        baseCost = kruskal(-1, -1)

        critical = []

        pseudo = []

        # test every edge
        for i in range(len(newEdges)):

            # critical edge test
            if kruskal(i, -1) > baseCost:

                critical.append(
                    newEdges[i][3]
                )

            # pseudo-critical edge test
            elif kruskal(-1, i) == baseCost:

                pseudo.append(
                    newEdges[i][3]
                )

        return [critical, pseudo]