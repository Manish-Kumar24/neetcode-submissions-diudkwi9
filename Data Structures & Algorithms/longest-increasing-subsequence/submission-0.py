class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        t = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    t[i] = max(t[i], t[j] + 1)
        return max(t)