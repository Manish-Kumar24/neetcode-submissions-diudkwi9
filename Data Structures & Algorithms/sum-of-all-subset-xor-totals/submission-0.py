class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(idx, currXor):
            # base case
            if idx == n:
                return currXor
            # include
            include = backtrack(idx+1, currXor ^ nums[idx])
            # exclude
            exclude = backtrack(idx+1, currXor)
            return include + exclude
        n = len(nums)
        return backtrack(0, 0)