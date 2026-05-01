class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(idx, tmp, currSum):
            # base case
            if currSum == target:
                res.append(tmp[:])
                return
            if currSum > target or idx == n:
                return
            # include (same index allowed)
            tmp.append(nums[idx])
            backtrack(idx, tmp, currSum + nums[idx])
            tmp.pop()
            # not include → move forward
            backtrack(idx + 1, tmp, currSum)
        res = []
        n = len(nums)
        backtrack(0, [], 0)
        return res