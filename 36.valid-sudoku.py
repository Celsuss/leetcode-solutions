#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List
import numpy as np

board_length = 9

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board = np.array(board)

        if not self.isRowsValid(board):
            return False
        if not self.isColumnsValid(board):
            return False
        if not self.isSubBoxValid(board):
            return False

        return True

    def isRowsValid(self, board: np.array) -> bool:
        for row in board:
            if not self.containsNoDuplicates(row):
                return False
        return True

    def isColumnsValid(self, board: np.array) -> bool:
        for column in board.T:
            if not self.containsNoDuplicates(column):
                return False
        return True

    def isSubBoxValid(self, board: np.array) -> bool:
        for i in range(0, board_length, 3):
            for j in range(0, board_length, 3):
                sub_box = board[i:i+3, j:j+3].flatten()
                if not self.containsNoDuplicates(sub_box):
                    return False

        return True

    def containsNoDuplicates(self, values: np.array) -> bool:
        values_set = set()
        for v in values:
            if v != '.' and v in values_set:
                return False
            else:
                values_set.add(v)
        return True
        
# @lc code=end

def main():
    s = Solution()
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    expected = True
    res = s.isValidSudoku(board)
    assert(res == expected)

    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    expected = False
    res = s.isValidSudoku(board)
    assert(res == expected)

    return 0

if __name__ == '__main__':
    main()
