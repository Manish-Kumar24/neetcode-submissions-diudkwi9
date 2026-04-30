class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a > 0: heapq.heappush(maxHeap, (-a, 'a'))
        if b > 0: heapq.heappush(maxHeap, (-b, 'b'))
        if c > 0: heapq.heappush(maxHeap, (-c, 'c'))
        res = []
        while maxHeap:
            cnt1, ch1 = heapq.heappop(maxHeap)
            if len(res) >= 2 and res[-1] == res[-2] == ch1:
                if not maxHeap: break
                cnt2, ch2 = heapq.heappop(maxHeap)
                res.append(ch2)
                cnt2 += 1
                if cnt2 < 0: heapq.heappush(maxHeap, (cnt2, ch2))
                heapq.heappush(maxHeap, (cnt1, ch1))
            else:
                res.append(ch1)
                cnt1 += 1
                if cnt1 < 0: heapq.heappush(maxHeap, (cnt1, ch1))
        return ''.join(res)