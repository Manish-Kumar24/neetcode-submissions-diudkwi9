from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        @cache
        def dfs(l, r):
            if l > r:
                return 0
            ans = 0
            for k in range(l, r + 1):
                ans = max(
                    ans,
                    dfs(l, k - 1)
                    + dfs(k + 1, r)
                    + nums[l - 1] * nums[k] * nums[r + 1]
                )
            return ans
        return dfs(1, len(nums) - 2)