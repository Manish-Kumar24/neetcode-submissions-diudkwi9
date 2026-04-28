class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)       # first largest
            x = -heapq.heappop(maxHeap)       # second largest
            if y != x:
                heapq.heappush(maxHeap, -(y-x))
        return -maxHeap[0] if maxHeap else 0