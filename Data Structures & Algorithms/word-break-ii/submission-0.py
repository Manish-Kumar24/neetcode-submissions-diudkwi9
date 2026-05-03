class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        res = []
        n = len(s)
        def backtrack(idx, tmp):
            if idx == n:
                res.append(" ".join(tmp))
                return
            for j in range(idx+1, n+1):
                word = s[idx:j]
                if word in wordSet:
                    tmp.append(word)
                    backtrack(j, tmp)
                    tmp.pop()
        backtrack(0, [])
        return res