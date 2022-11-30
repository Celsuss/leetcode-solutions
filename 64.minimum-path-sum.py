#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        # Prepare grid
        costs = [[10000] * (len(grid[0])+1) for i in range(len(grid)+1)]
        costs[-1][-2] = 0

        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[i]) - 1, -1, -1):
                costs[i][j] = grid[i][j] + min(costs[i][j+1], costs[i+1][j])

                continue


        return costs[0][0]
        
# @lc code=end

def main():
    s = Solution()

    grid = [[1,3,1],[1,5,1],[4,2,1]]
    out = s.minPathSum(grid)
    assert(out == 7)

    grid = [[1,2,3],[4,5,6]]
    out = s.minPathSum(grid)
    assert(out == 12)

    return 0

if __name__ == '__main__':
    main()