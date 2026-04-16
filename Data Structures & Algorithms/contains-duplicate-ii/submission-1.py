class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Brute Force -> O(n^2)/O(1)
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             if abs(j-i) <= k:
        #                 return True
        # return False
        
        # Optimal(using hashmap) -> O(n)/O(n)
        mp = {}
        for i, num in enumerate(nums):
            if num in mp and i - mp[num] <= k:
                return True
            mp[num] = i
        return False