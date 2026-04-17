class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Cyclic Sort -> O(n)/O(1)
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                corrIdx = nums[i] - 1
                nums[i], nums[corrIdx] = nums[corrIdx], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1