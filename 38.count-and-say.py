"""
The count-and-say sequence is a sequence of digit strings defined by the
recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
run-length encoding (RLE) is a string compression method that works by
replacing consecutive identical characters (repeated 2 or more times) with the
concatenation of the character and the number marking the count of the
characters (length of the run). For example, to compress the string "3322251"
we replace "33" with "23", replace "222" with "32", replace "5" with "15" and
replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say
sequence.

Example 1:

Input: n = 4
Output: "1211"

Explanation:
countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"

Example 2:

Input: n = 1
Output: "1"

Explanation:
This is the base case.
"""


# @lc code=start
class Solution:
    """Solution to be submitted."""

    def countAndSay(self, n: int) -> str:
        """Solution for problem."""
        if n <= 0:
            return ""
        res = "1"
        for i in range(2, n+1):
            res = self.rle(res)
            continue
        return res

    def rle(self, s: str) -> str:
        """Calculate Run-length encoding."""
        res = ''
        prev_c = s[0]
        count = 0
        for c in s:
            if c != prev_c:
                res += f'{count}{prev_c}'
                prev_c = c
                count = 1
            else:
                count += 1

        if count != 0:
            res += f'{count}{c}'

        return res
# @lc code=end


def main():
    """Test function."""
    s = Solution()

    n = 1
    res = s.countAndSay(n)
    expected = "1"
    assert res == expected

    n = 4
    res = s.countAndSay(n)
    expected = "1211"
    assert res == expected

    n = 5
    res = s.countAndSay(n)
    expected = "111221"
    assert res == expected

    print('success')
    return 0


if __name__ == "__main__":
    main()
