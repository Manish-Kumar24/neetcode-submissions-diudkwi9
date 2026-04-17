class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9    ## no. of rows, cols, boes in sudoku
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]
        for r in range(n):
            for c in range(n):
                val = board[r][c]
                if val == ".":
                    continue
                box = (r // 3) * 3 + (c // 3)
                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)
        return True