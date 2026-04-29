class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)
        time, q = 0, deque()
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt < 0:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time