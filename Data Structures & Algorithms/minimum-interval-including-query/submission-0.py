class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        res = [-1] * len(queries)
        heap = []
        i = 0
        for q, idx in sorted_queries:
            # Step 1: add valid intervals
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                length = end - start + 1
                heapq.heappush(heap, (length, end))
                i += 1
            # Step 2: remove invalid intervals
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            # Step 3: answer
            if heap:
                res[idx] = heap[0][0]
        return res