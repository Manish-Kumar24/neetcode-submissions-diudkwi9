class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(tmp):
            if len(tmp) == n:
                res.append(tmp[:])
                return
            for i in range(n):
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                if used[i]:
                    continue
                used[i] = True
                tmp.append(nums[i])
                backtrack(tmp)
                tmp.pop()
                used[i] = False
        nums.sort()
        res = []
        n = len(nums)
        used = [False] * n
        backtrack([])
        return res