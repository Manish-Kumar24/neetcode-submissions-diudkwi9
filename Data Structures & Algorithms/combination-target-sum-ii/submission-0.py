class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(idx, tmp, currSum):
            # base case
            if currSum == target:
                res.append(list(tmp))
                return 
            if currSum > target or idx == n:
                return
            # include
            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                tmp.append(candidates[i])
                backtrack(i+1, tmp, currSum + candidates[i])
                tmp.pop()
        candidates.sort()
        res = []
        n = len(candidates)
        backtrack(0, [], 0)
        return res