class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, n, idx, tmp):
            if idx == n:
                res.append(tmp[:])
                return
            # not include
            backtrack(nums, n, idx+1, tmp)
            # include
            tmp.append(nums[idx])
            backtrack(nums, n, idx+1, tmp)
            tmp.pop()
        n = len(nums)
        res = []
        backtrack(nums, n, 0, [])
        return res