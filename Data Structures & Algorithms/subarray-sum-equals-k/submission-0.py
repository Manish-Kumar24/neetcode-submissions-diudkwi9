class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Brute Force -> O(n^2)
        # n = len(nums)
        # cnt = 0
        # for i in range(n):
        #     total = 0
        #     for j in range(i, n):
        #         total += nums[j]
        #         if total == k:
        #             cnt += 1
        # return cnt

        # Optimized Approach(using prefix sum) -> O(n)/O(n)
        mp = {0:1}
        prefixSum = 0
        cnt = 0
        for num in nums:
            prefixSum += num
            if prefixSum-k in mp:
                cnt += mp[prefixSum-k]
            mp[prefixSum] = mp.get(prefixSum, 0) + 1
        return cnt