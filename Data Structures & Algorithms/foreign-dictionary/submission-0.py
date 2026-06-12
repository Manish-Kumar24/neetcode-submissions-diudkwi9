class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        indeg = {c:0 for c in adj}
        for u in adj:
            for v in adj[u]:
                indeg[v] += 1
        q = deque()
        for c in indeg:
            if indeg[c] == 0:
                q.append(c)
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nbr in adj[node]:
                indeg[nbr] -= 1
                if indeg[nbr] == 0:
                    q.append(nbr)
        return "".join(res) if len(res) == len(adj) else ""