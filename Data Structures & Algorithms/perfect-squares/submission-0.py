class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for amt in range(1, n + 1):
            for sq in squares:
                if sq <= amt:
                    dp[amt] = min(
                        dp[amt],
                        1 + dp[amt - sq]
                    )
        return dp[n]