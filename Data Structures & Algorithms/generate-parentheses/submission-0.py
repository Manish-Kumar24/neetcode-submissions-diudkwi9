class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(Open, Close, tmp, res):
            if Open == n and Close == n:
                res.append("".join(tmp))
            if Open < n:
                tmp.append("(")
                backtrack(Open+1, Close, tmp, res)
                tmp.pop()
            if Close < Open:
                tmp.append(")")
                backtrack(Open, Close+1, tmp, res)
                tmp.pop()
        res = []
        backtrack(0, 0, [], res)
        return res