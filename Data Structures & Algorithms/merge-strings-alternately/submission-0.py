class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newStr = []
        m, n = len(word1), len(word2)
        i, j = 0, 0
        while i < m and j < n:
            newStr.append(word1[i])
            newStr.append(word2[j])
            i += 1
            j += 1
        while i < m:
            newStr.append(word1[i])
            i += 1
        while j < n:
            newStr.append(word2[j])
            j += 1
        return "".join(newStr)