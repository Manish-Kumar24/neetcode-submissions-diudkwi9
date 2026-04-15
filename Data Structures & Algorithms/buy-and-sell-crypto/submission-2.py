class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force -> O(n^2)/O(1)
        # profit = 0
        # n = len(prices)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if prices[j] - prices[i] > 0:
        #             profit = max(profit, prices[j]-prices[i])
        # return profit

        # Optimal(One Pass) -> O(n)/O(1)
        # minPrice, maxProfit = float('inf'), 0
        # for price in prices:
        #     minPrice = min(minPrice, price)
        #     maxProfit = max(maxProfit, price - minPrice)
        # return maxProfit

        # Two Pointer -> O(n)/O(1)
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxProfit