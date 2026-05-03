class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row):
            cnt = 0
            # base case
            if row == n:
                return 1
            for col in range(n):
                if col in cols or (row-col) in diag1 or (row+col) in diag2:
                    continue
                # add
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)
                cnt += backtrack(row+1)
                # remove
                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)
            return cnt
        cols = set()
        diag1 = set()
        diag2 = set()
        return backtrack(0)