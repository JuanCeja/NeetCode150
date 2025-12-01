# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

def is_valid_sudoku(board: list[list]) -> bool:
    hash_set = {}

    for r in range(len(board)):
        for c in range(len(board)):
            coordinates = (r // 3, c // 3)

            if board[r][c] == ".":
                continue

            if coordinates not in hash_set:
                hash_set[coordinates] = set()
                hash_set[coordinates].add(int(board[r][c]))
            elif int(board[r][c]) in hash_set[coordinates]:
                return False
            else:
                hash_set[coordinates].add(int(board[r][c]))

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