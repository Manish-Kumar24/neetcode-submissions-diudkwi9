class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < abs(target):
            return 0
        if (target + total) % 2:
            return 0
        subset = (total + target) // 2
        dp = [0] * (subset + 1)
        dp[0] = 1
        for num in nums:
            for s in range(subset, num-1, -1):
                dp[s] += dp[s - num]
        return dp[subset]