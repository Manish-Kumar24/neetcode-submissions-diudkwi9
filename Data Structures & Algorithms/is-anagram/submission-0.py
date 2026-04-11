class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using 2 hashmap -> O(n) / O(n)
        # if len(s) != len(t):
        #     return False
        # mp1 = {}
        # mp2 = {}
        # for ch in s:
        #     mp1[ch] = mp1.get(ch, 0) + 1
        # for ch in t:
        #     mp2[ch] = mp2.get(ch, 0) + 1
        # return mp1 == mp2

        # using 1 hashmap -> O(n) / O(n)
        if len(s) != len(t):
            return False
        mp = {}
        for ch in s:
            mp[ch] = mp.get(ch, 0) + 1
        for ch in t:
            if ch not in mp:
                return False
            mp[ch] -= 1
            if mp[ch] == 0:
                del mp[ch]
        return len(mp) == 0