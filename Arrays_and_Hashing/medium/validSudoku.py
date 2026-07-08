# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

from collections import defaultdict


def is_valid_sudoku(board: list[list[str]]) -> bool:
    rows_seen = set()
    cols_seen = set()
    boxes_seen = set()

    for r, row in enumerate(board):
        for c, val in enumerate(row):
            if val == ".":
                continue

            if (r, val) in rows_seen:
                return False
            rows_seen.add((r, val))

            if (c, val) in cols_seen:
                return False
            cols_seen.add((c, val))

            box_row = r // 3
            box_col = c // 3

            if (box_row, box_col, val) in boxes_seen:
                return False
            boxes_seen.add((box_row, box_col, val))

    return True


board_1 = [["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","8",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",".","5"],
            ["7",".",".",".","2",".",".",".","6"],
            [".",".",".",".",".",".","2",".","."],
            [".",".",".","4","1","9",".",".","8"],
            [".",".",".",".","8",".",".","7","9"]]

board_2 = [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","1",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]


print(is_valid_sudoku(board_1)) # true
print(is_valid_sudoku(board_2)) # false