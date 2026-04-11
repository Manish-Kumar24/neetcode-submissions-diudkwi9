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

        # using map + minHeap -> O(nlogk)
        # mp = {}
        # for num in nums:
        #     mp[num] = mp.get(num, 0) + 1
        # minHeap = []
        # res = []
        # for key, val in mp.items():
        #     heapq.heappush(minHeap, (val, key))
        #     if len(minHeap) > k:
        #         heapq.heappop(minHeap)
        # while minHeap:
        #     res.append(heapq.heappop(minHeap)[1])
        # return res

        # using bucket sort -> O(n)
        # Step 1: frequency map
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        # Step 2: create buckets
        # index = frequency, value = list of numbers
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in mp.items():
            bucket[freq].append(num)
        # Step 3: collect top k from back
        res = []
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res