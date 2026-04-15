class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute Force -> O(n^2)/O(n)
        n = len(s)
        maxL = 0
        for i in range(n):
            freq  = {}
            maxfreq = 0
            for j in range(i, n):
                freq[s[j]] = freq.get(s[j], 0) + 1
                maxfreq = max(maxfreq, freq[s[j]])
                window = j - i + 1
                if window - maxfreq <= k:
                    maxL = max(maxL, window)
                else:
                    break
        return maxL