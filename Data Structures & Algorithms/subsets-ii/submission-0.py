class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, tmp):
            res.append(tmp[:])
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                tmp.append(nums[i])
                backtrack(i+1, tmp)
                tmp.pop()
        res = []
        nums.sort()
        n = len(nums)
        backtrack(0, [])
        return res