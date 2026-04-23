class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k):
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / k)
            return hrs <= h
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if canFinish(mid):
                high = mid
            else:
                low = mid + 1
        return low