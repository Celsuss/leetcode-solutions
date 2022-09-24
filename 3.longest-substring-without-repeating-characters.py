#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
from multiprocessing.context import assert_spawning
from re import sub


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        best_substr_length = 0
        substr_set = set()
        substr = ''

        for c in s:
            if c in substr:
                best_substr_length = self.getBestSubstrLength(len(substr), best_substr_length)
                substr = self.shrinkSubStr(substr, substr_set, c)

            substr_set.add(c)
            substr += c

        best_substr_length = self.getBestSubstrLength(len(substr), best_substr_length)

        return best_substr_length

    def shrinkSubStr(self, substr, substr_set, c):
        # Remove each element from start of array until we find duplicate character
        for i in range(len(substr)):
            i_c = substr[i]
            substr_set.discard(i_c)
            if i_c == c:
                substr = substr[i+1:]
                return substr
        return substr

    def getBestSubstrLength(self, length, best_length):
        if length > best_length:
            return length
        return best_length
        
# @lc code=end

def main():
    s = Solution()

    data = "dvdf"
    res = s.lengthOfLongestSubstring(data)
    assert(res == 3)

    data = "au"
    res = s.lengthOfLongestSubstring(data)
    assert(res == 2)

    data = " "
    res = s.lengthOfLongestSubstring(data)
    assert(res == 1)

    data = "abcabcbb"
    res = s.lengthOfLongestSubstring(data)
    assert(res == 3)

    data = "bbbbb"
    res = s.lengthOfLongestSubstring(data)
    assert(res == 1)

    data = "pwwkew"
    res = s.lengthOfLongestSubstring(data)
    assert(res == 3)

    return

if __name__ == '__main__':
    main()