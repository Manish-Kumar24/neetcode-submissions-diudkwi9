class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(sub):
            return sub == sub[::-1]
        def backtrack(start, tmp):
            if start == n:
                res.append(tmp[:])
                return
            for end in range(start, n):
                substring = s[start:end+1]
                if isPalindrome(substring):
                    tmp.append(substring)
                    backtrack(end + 1, tmp)
                    tmp.pop()
        n = len(s)
        res = []
        backtrack(0, [])
        return res