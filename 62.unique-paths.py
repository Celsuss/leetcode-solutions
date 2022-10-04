#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        w = n
        h = m

        prev_row = [1] * w
        for i in range(h-1):
            row = [1] * w
            for j in range(w-1):
                row[w-j-2] = prev_row[w-j-2] + row[w-j-1]
                continue

            prev_row = row
            continue

        return prev_row[0]
        
# @lc code=end

def main():
    s = Solution()

    m = 3
    n = 2
    out = s.uniquePaths(m, n)
    assert(out == 3)

    m = 3
    n = 7
    out = s.uniquePaths(m, n)
    assert(out == 28)

    m = 7
    n = 3
    out = s.uniquePaths(m, n)
    assert(out == 28)

    return 0

if __name__ == '__main__':
    main()