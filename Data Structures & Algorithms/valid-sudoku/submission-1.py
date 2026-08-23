class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = {}

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                square = (r // 3, c // 3)

                if square not in squares:
                    squares[square] = set()

                if (
                    value in rows[r]
                    or value in cols[c]
                    or value in squares[square]
                ):
                    return False

                rows[r].add(value)
                cols[c].add(value)
                squares[square].add(value)

        return True