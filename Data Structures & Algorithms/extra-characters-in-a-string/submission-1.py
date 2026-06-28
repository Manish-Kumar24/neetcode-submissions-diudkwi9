class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        n = len(s)
        memo = {}
        def dfs(i):
            if i == n:
                return 0
            if i in memo:
                return memo[i]
            ans = 1 + dfs(i + 1)
            for j in range(i + 1, n + 1):
                if s[i:j] in words:
                    ans = min(ans, dfs(j))
            memo[i] = ans
            return ans
        return dfs(0)