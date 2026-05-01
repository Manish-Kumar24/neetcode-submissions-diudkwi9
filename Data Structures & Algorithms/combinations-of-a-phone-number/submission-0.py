class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        f = {
            "2":"abc", "3":"def", "4":"ghi", "5":"jkl",
            "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"
        }
        def backtrack(idx, tmp):
            if idx == n:
                res.append("".join(tmp))
                return
            choices = f[digits[idx]]
            for j in range(len(choices)):
                tmp.append(choices[j])
                backtrack(idx+1, tmp)
                tmp.pop()
        n = len(digits)
        res = []
        backtrack(0, [])
        return res