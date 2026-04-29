class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)
        time = 0
        while maxHeap:
            temp = []
            for _ in range(n + 1):
                if maxHeap:
                    temp.append(heapq.heappop(maxHeap) + 1)  
            for f in temp:
                if f < 0:
                    heapq.heappush(maxHeap, f)
            if not maxHeap:
                time += len(temp)
            else:
                time += (n + 1)
        return time