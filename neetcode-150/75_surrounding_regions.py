# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
#
# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
#
# Example 1:
#
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
#
# Explanation:
#
# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.
#
# Example 2:
#
# Input: board = [["X"]]
#
# Output: [["X"]]
#
# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        for row in range(len(board)):
            self.dfs(board, row, 0)
            self.dfs(board, row, len(board[0]) - 1)

        for col in range(len(board[0])):
            self.dfs(board, 0, col)
            self.dfs(board, len(board) - 1, col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O' :
                    board[row][col] = 'X'
                if board[row][col] == 'T' :
                    board[row][col] = 'O'

        return board


    def dfs(self, board, row, col):
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != 'O':
            return
        board[row][col] = 'T'
        self.dfs(board, row - 1, col)
        self.dfs(board, row + 1, col)
        self.dfs(board, row, col - 1)
        self.dfs(board, row, col + 1)


