class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(tmp):
            if len(tmp) == n:
                res.append(tmp[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                tmp.append(nums[i])
                backtrack(tmp)
                tmp.pop()
                used[i] = False
        res = []
        n = len(nums)
        used = [False] * n
        backtrack([])
        return res