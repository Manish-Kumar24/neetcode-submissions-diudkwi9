class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            # base case
            if row == n:
                board = ["".join(r) for r in grid]
                res.append(board)
                return
            for col in range(n):
                if col in cols or (row-col) in diag1 or (row+col) in diag2:
                    continue
                # add 
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)
                grid[row][col] = "Q"
                backtrack(row+1)
                # remove
                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)
                grid[row][col] = "."
        res = []
        grid = [["."] * n for _ in range(n)]
        cols = set()
        diag1 = set()
        diag2 = set()
        backtrack(0)
        return res