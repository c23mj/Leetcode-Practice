class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    # print(f"val: {val}")
                    idx = j//3 + 3 * (i // 3)
                    # print(f"square: {idx}")
                    if val in rows[i] or val in cols[j] or val in squares[idx]:
                        # print(f"{val} is intersecting with one of: {rows[i]}, {cols[j]}, or {squares[idx]}")
                        return False
                    rows[i].add(val)
                    cols[j].add(val)
                    squares[idx].add(val)
        return True