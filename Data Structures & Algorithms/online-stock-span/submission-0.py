class StockSpanner:

    def __init__(self):
        self.stack = []
        self.i = -1

    def next(self, price: int) -> int:
        self.i += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        if not self.stack:
            span = self.i + 1
        else:
            span = self.i - self.stack[-1][1]
        self.stack.append((price, self.i))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)