class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a, b in prerequisites:
            adj[b].append(a)
            indeg[a] += 1
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nbr in adj[node]:
                indeg[nbr] -= 1
                if indeg[nbr] == 0:
                    q.append(nbr)
        if len(order) == numCourses:
            return order
        return []