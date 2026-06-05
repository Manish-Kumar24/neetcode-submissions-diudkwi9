class Solution:
    def minEnd(self, n: int, x: int) -> int:
        k = n - 1
        ans = x
        bitPos = 0
        while k:
            if (x & (1 << bitPos)) == 0:
                if k & 1:
                    ans |= (1 << bitPos)
                k >>= 1
            bitPos += 1
        return ans