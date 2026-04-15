class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute Force -> O(n^2)/O(n)
        # n = len(s)
        # maxL = 0
        # for i in range(n):
        #     freq  = {}
        #     maxfreq = 0
        #     for j in range(i, n):
        #         freq[s[j]] = freq.get(s[j], 0) + 1
        #         maxfreq = max(maxfreq, freq[s[j]])
        #         window = j - i + 1
        #         if window - maxfreq <= k:
        #             maxL = max(maxL, window)
        #         else:
        #             break
        # return maxL

        # Use one loop -> 
        
        n, low, f, res = len(s), 0, [0]*26, 0
        def find(a):
            maxi = 0
            for i in range(len(a)):
                maxi = max(maxi, a[i])
            return maxi
        for high in range(n):
            f[ord(s[high]) - ord('A')] += 1
            while (high - low + 1) - find(f) > k:
                f[ord(s[low]) - ord('A')] -= 1
                low += 1
            res = max(res, high - low + 1)
        return res