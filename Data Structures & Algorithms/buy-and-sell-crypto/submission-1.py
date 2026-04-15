class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        for i in range(n-1):
            for j in range(i+1, n):
                if prices[j] - prices[i] > 0:
                    profit = max(profit, prices[j]-prices[i])
        return profit