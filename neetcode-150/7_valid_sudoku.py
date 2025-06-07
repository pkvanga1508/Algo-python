# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

class Solution(object):
    def isValidSudoku(self, board):
        row_set = [set() for _ in range(0,9)]
        col_set = [set() for _ in range(0,9)]
        box_set = [set() for _ in range(0,9)]
        for row in range(len(board)):
            for col in range(len(board[0])):
                value = board[row][col]

                if value == '.':
                    continue

                if value in row_set[row]:
                    print(row, col, value, row_set)
                    return False
                row_set[row].add(value)

                if value in col_set[col]:
                    print(row, col, value, row_set)
                    return False
                col_set[col].add(value)

                box_set_index = ((row // 3) * 3) + (col // 3)

                if value in box_set[box_set_index]:
                    print(row, col, value, box_set)
                    return False
                box_set[box_set_index].add(value)

        return True


