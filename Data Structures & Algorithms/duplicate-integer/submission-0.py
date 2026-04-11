class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(nlogn) / O(1)
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

        # O(n) / o(n)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False