class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        count = [i for i in range(1, n+1)]
        def backtrack(idx, tmp):
            if len(tmp) == k:
                res.append(list(tmp))
            for i in range(idx, n+1):
                tmp.append(i)
                backtrack(i+1, tmp)
                tmp.pop()
        res = []
        backtrack(1, [])
        return res