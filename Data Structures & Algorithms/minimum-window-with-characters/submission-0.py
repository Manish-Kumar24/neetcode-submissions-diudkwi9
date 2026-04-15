class Solution:
    def minWindow(self, s, t):
        need = [0]*128
        for c in t:
            need[ord(c)] += 1
        l = 0
        count = len(t)
        min_len = float('inf')
        start = 0
        for r in range(len(s)):
            if need[ord(s[r])] > 0:
                count -= 1
            need[ord(s[r])] -= 1
            while count == 0:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l
                need[ord(s[l])] += 1
                if need[ord(s[l])] > 0:
                    count += 1
                l += 1
        return "" if min_len == float('inf') else s[start:start+min_len]