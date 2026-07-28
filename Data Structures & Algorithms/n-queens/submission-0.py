class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        cols = set()
        posDiag = set()
        negDiag = set()

        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):

                if col in cols:
                    continue

                if row + col in posDiag:
                    continue

                if row - col in negDiag:
                    continue

                cols.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)

                board[row][col] = "Q"

                backtrack(row + 1)

                board[row][col] = "."
                cols.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)

        backtrack(0)

        return result
        