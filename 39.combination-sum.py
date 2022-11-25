#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        out = []
        candidates

        for i in range(len(candidates)-1, 0, -1):
            self.backtrack(candidates, [candidates[i]], target, out)

        return out

    def backtrack(self, candidates: list[int], current: list[int], target: int, solutions: list[list[int]]):
        current_sum = sum(current)
        if current_sum == target:
            solutions.append(current[:])
            return -1
        if current_sum > target:
            return -1

        for i in range(len(candidates)):
            current.append(candidates[i])
            res = self.backtrack(candidates, current, target, solutions)
            current.pop()
            if res == -1:
                break
        
        return 0
        
# @lc code=end

def main():
    s = Solution()

    candidates = [2,3,6,7]
    target = 7
    out = s.combinationSum(candidates, target)
    assert(out == [[7],[3,2,2]])

    candidates = [2,3,5]
    target = 8
    out = s.combinationSum(candidates, target)
    assert(out == [[2,2,2,2],[2,3,3],[3,5]])

    candidates = [2]
    target = 1
    out = s.combinationSum(candidates, target)
    assert(out == [])

    return 0

if __name__ == '__main__':
    main()