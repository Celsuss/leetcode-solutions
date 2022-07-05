#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#

# @lc code=start
from typing import Tuple

class Solution:
    def minDeletions(self, s: str) -> int:
        char_count = self.countCharacters(s)
        min_deletions = 0
        values = self.getValuesSet(char_count)

        c, v = self.getNextDuplicateValue(char_count)

        while c != '':
            subtraction = self.subtract(char_count, values, s, c, v)
            min_deletions = min_deletions + subtraction
            c, v = self.getNextDuplicateValue(char_count)


        return min_deletions

    def getNextDuplicateValue(self, char_count: dict) -> Tuple[str, int]:
        values = set()
        next_duplicate_value = ('', -1)

        for c in list(char_count.keys()):
            val = char_count[c]
            if val != 0 and val in values and (val < next_duplicate_value[1] or next_duplicate_value[1] == -1):
                next_duplicate_value = (c, val)
            else:
                values.add(val)
        return next_duplicate_value

    def subtract(self, char_count: dict, values: set, s: str, c: str, v: str):
        updated_v = v
        while updated_v > -1:
            if updated_v in values and updated_v != 0:
                updated_v = updated_v-1
            else:
                delta = v - updated_v
                s.replace(c, '', delta)
                values.add(updated_v)
                char_count[c] = updated_v
                break

        return v - updated_v

    def getValuesSet(self, char_count: dict) -> set():
        values = set()
        for c in char_count:
            values.add(char_count[c])
        return values

    def countCharacters(self, s: str) -> dict:
        char_count = {}
        for c in s:
            if c not in char_count:
                char_count[c] = 0
            char_count[c] += 1
        return char_count
        
# @lc code=end

def main():
    s = Solution()

    test_input = 'bbcebab'
    val = s.minDeletions(test_input)
    print('Result: {} from string: {}'.format(val, test_input))

    test_input = 'aaabbbcc'
    val = s.minDeletions(test_input)
    print('Result: {} from string: {}'.format(val, test_input))

    return 0

if __name__ == '__main__':
    main()