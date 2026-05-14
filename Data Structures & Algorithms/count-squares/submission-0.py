from collections import defaultdict

class CountSquares:

    def __init__(self):

        self.cnt = defaultdict(int)

    def add(self, point: List[int]) -> None:

        x, y = point

        self.cnt[(x, y)] += 1

    def count(self, point: List[int]) -> int:

        x1, y1 = point

        ans = 0

        for (x2, y2), freq in self.cnt.items():

            # valid diagonal
            if (
                abs(x1 - x2) == abs(y1 - y2)
                and x1 != x2
            ):

                ans += (
                    freq *
                    self.cnt.get((x1, y2), 0) *
                    self.cnt.get((x2, y1), 0)
                )

        return ans