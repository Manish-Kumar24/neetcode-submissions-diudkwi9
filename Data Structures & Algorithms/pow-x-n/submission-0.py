class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        power = abs(n)
        ans = 1
        for _ in range(power):
            ans *= x
        if n < 0:
            return 1/ans
        return ans