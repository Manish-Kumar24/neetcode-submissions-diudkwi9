class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute Force -> O(n^2)/O(n)
        # n = len(s)
        # maxL = 0
        # for i in range(n):
        #     seen = set()
        #     for j in range(i, n):
        #         if s[j] in seen:
        #             break
        #         seen.add(s[j])
        #         maxL = max(maxL, j-i+1)
        # return maxL

        # Optimal Approach ->O(n)/O(n)
        # l, maxL = 0, 0
        # mp = {}
        # for r in range(len(s)):
        #     if s[r] in mp:
        #         l = max(l, mp[s[r]]+1)
        #     mp[s[r]] = r
        #     maxL = max(maxL, r-l+1)
        # return maxL

        # Best approach(use ASCII index) -> O(n)/O(1)
        maxL, l, idx = 0, 0, [-1] * 128
        for r in range(len(s)):
            l = max(l, idx[ord(s[r])]+1)
            idx[ord(s[r])] = r
            maxL = max(maxL, r-l+1)
        return maxL