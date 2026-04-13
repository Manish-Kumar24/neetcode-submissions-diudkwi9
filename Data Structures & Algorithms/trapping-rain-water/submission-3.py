class Solution:
    def trap(self, ht: List[int]) -> int:
        # # Better Approach -> O(n)/O(n)
        # n = len(ht)
        # if n == 0:
        #     return 0
        # lmax, rmax = [0]*n, [0]*n
        # # build lmax
        # lmax[0] = ht[0]
        # for i in range(1, n):
        #     lmax[i] = max(lmax[i-1], ht[i])
        # # build rmax
        # rmax[n-1] = ht[n-1]
        # for i in range(n-2, -1, -1):
        #     rmax[i] = max(rmax[i+1], ht[i])
        # # traverse
        # ans = 0
        # for i in range(n):
        #     ans += min(lmax[i], rmax[i]) - ht[i]
        # return ans

        # Optimal Approach -> O(n)/O(1)
        n = len(ht)
        if n == 0:
            return 0
        l, r = 0, n-1
        lmax, rmax = 0, 0
        ans = 0
        while l < r:
            lmax = max(lmax, ht[l])
            rmax = max(rmax, ht[r])
            if lmax < rmax:
                ans += lmax - ht[l]
                l += 1
            else:
                ans += rmax - ht[r]
                r -= 1
        return ans