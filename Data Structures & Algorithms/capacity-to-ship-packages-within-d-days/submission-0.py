class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            daysUsed = 1
            currWt = 0
            for w in weights:
                if currWt + w > capacity:
                    daysUsed += 1
                    currWt = 0
                currWt += w
            return daysUsed <= days
        low, high = max(weights), sum(weights)
        while low < high:
            mid = (low + high) // 2
            if canShip(mid):
                high = mid
            else:
                low = mid + 1
        return low