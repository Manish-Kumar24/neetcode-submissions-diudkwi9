class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a, b in prerequisites:
            adj[b].append(a)
            indeg[a] += 1
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        completed = 0
        while q:
            node = q.popleft()
            completed += 1
            for nbr in adj[node]:
                indeg[nbr] -= 1
                if indeg[nbr] == 0:
                    q.append(nbr)
        return completed == numCourses