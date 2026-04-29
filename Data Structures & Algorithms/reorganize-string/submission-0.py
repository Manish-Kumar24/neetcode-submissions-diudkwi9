class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        maxHeap = [(-cnt, ch) for ch, cnt in freq.items()]
        heapq.heapify(maxHeap)
        prev = (0, "")
        res = []
        while maxHeap:
            cnt, ch = heapq.heappop(maxHeap)
            res.append(ch)
            if prev[0] < 0:
                heapq.heappush(maxHeap, prev)
            cnt += 1
            prev = (cnt, ch)
        result = "".join(res)
        return result if len(result) == len(s) else ""