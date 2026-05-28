class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        inf = float('inf')
        t = [[inf] * (amount+1) for _ in range(n+1)]
        for i in range(n+1):
            t[i][0] = 0
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:
                    t[i][j] = min(1 + t[i][j-coins[i-1]], t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        return t[n][amount] if t[n][amount] != inf else -1