#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start


class Solution:
    def numTrees(self, n: int) -> int:
        i_nodes_trees = [1] * (n + 1)

        # First two trees is always 1
        for i in range(2, n+1):
            total = 0
            for root in range(i):
                left = root
                right = i - (root+1)
                total += i_nodes_trees[left] * i_nodes_trees[right]
            i_nodes_trees[i] = total

            continue

        return i_nodes_trees[n]
        
# @lc code=end

def main():
    s = Solution()

    n = 4
    res = s.numTrees(n)
    assert(res == 14)
    
    n = 3
    res = s.numTrees(n)
    assert(res == 5)

    n = 1
    res = s.numTrees(n)
    assert(res == 1)

    return


if __name__ == '__main__':
    main()