#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Get target row
        target_row = self.getTargetRow(matrix, target)
        if target_row is None:
            return False

        target_column = self.getTargetColumn(matrix[target_row], target)
        if target_column is None:
            return False

        return True

    def getTargetRow(self, matrix: list[list[int]], target: int) -> int:
        n_rows = len(matrix)

        for i in range(n_rows):
            test = matrix[i][-1]
            if matrix[i][-1] >= target:
                return i
        return None

    def getTargetColumn(self, row: list[int], target: int) -> int:
        for i in range(len(row)):
            if row[i] == target:
                return i
        return None
        
# @lc code=end

def main():
    s = Solution()

    res = s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3)
    assert res == True

    res = s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13)

    return 0

if __name__ == '__main__':
    main()
