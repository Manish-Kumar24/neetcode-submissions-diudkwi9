class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def isValid(i, j):
            if i<0 or i>= m or j<0 or j>=n:
                return False
            return True
        def dfs(i, j):
            board[i][j] = '#'
            for dx, dy in dirs:
                row = i + dx
                col = j + dy
                if isValid(row, col) and board[row][col] == 'O':
                    dfs(row, col)
        # first row
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
        # last row
        for j in range(n):
            if board[m-1][j] == 'O':
                dfs(m-1, j)
        # first col
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
        # last col
        for i in range(m):
            if board[i][n-1] == 'O':
                dfs(i, n-1)
        # merge all
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        return 