class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        tasks.sort()
        res, minHeap = [], []
        time, i, n = 0, 0, len(tasks)
        while i < n or minHeap:
            if not minHeap: time = max(time, tasks[i][0])
            while i < n and tasks[i][0] <= time:
                et, pt, idx = tasks[i]
                heapq.heappush(minHeap, (pt, idx))
                i += 1
            pt, idx = heapq.heappop(minHeap)
            time += pt
            res.append(idx)
        return res