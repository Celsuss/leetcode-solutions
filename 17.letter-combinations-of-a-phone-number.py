#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []

        hashmap = self.getHashMap()
        res = []

        def propagateTree(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            for c in hashmap[digits[i]]:
                propagateTree(i + 1, curStr + c)

        propagateTree(0, '')

        return res

    def getHashMap(self):
        return {
            '2': ['a','b','c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
# @lc code=end

def main():
    s = Solution()

    digits = "23"
    res = s.letterCombinations(digits)
    assert(res == ["ad","ae","af","bd","be","bf","cd","ce","cf"])

    digits = ""
    res = s.letterCombinations(digits)
    assert(res == [])

    digits = "2"
    res = s.letterCombinations(digits)
    assert(res == ["a","b","c"])

    return 0

if __name__ == '__main__':
    main()