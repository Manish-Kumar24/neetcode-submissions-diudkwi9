class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans