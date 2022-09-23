#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # if n == 1:
        #     return ["()"]

        res = ''
        res = self.generateTree(res, n, 0, 0)
        return res

    def generateTree(self, parenthesis: str, n: int, n_open: int, n_closed: int):
        if n_open == n_closed == n:
            return [parenthesis]

        res = []
        if n_open < n:
            res.extend(self.generateTree(parenthesis+'(', n, n_open+1, n_closed))
        if n_open > n_closed:
            res.extend(self.generateTree(parenthesis+')', n, n_open, n_closed+1))

        return res
        
# @lc code=end

def main():
    s = Solution()

    res = s.generateParenthesis(1)
    assert res == ["()"]

    res = s.generateParenthesis(3)
    assert res == ["((()))","(()())","(())()","()(())","()()()"]

    return 0


if __name__ == '__main__':
    main()