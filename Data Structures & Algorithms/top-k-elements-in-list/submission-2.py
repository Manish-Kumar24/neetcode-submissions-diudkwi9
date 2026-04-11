class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using sort -> O(nlogn)
        # mp = {}
        # res = []
        # for num in nums:
        #     mp[num] = mp.get(num, 0) + 1
        # sorted_items = sorted(mp.items(), key=lambda x:x[1], reverse=True)
        # for i in range(k):
        #     res.append(sorted_items[i][0])
        # return res

        # using map + minHeap
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        minHeap = []
        res = []
        for key, val in mp.items():
            heapq.heappush(minHeap, (val, key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        return res