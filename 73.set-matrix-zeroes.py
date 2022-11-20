#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_columns = len(matrix[0])     # n columns
        n_rows = len(matrix)  # n rows

        # Create arrays to flag rows and columns to be
        # set to 0.
        zero_columns = [1] * n_columns
        zero_rows = [1] * n_rows

        # Loop over the matrix and set flags
        for i in range(n_rows):
            for j in range(n_columns):
                if matrix[i][j] == 0:
                    zero_columns[j] = 0
                    zero_rows[i] = 0

        # Look at flags and set rows and columns to 0
        for i in range(n_rows):
            if zero_rows[i] == 0:
                zeros = [0] * n_columns
                matrix[i] = zeros

        for i in range(n_rows):
            for j in range(n_columns):
                if zero_columns[j] == 0:
                    matrix[i][j] = 0

        return
        
# @lc code=end

def main():
    s = Solution()

    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    s.setZeroes(matrix)
    assert(matrix == [[1,0,1],[0,0,0],[1,0,1]])

    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeroes(matrix)
    assert(matrix == [[0,0,0,0],[0,4,5,0],[0,3,1,0]])

    return 0

if __name__ == '__main__':
    main()