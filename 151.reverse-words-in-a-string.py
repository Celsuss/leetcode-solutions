"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be
 separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between
 two words. The returned string should only have a single space separating the
 words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing
 spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single
 space in the reversed string.
"""


# @lc code=start
class Solution:
    """Solution class."""

    def reverseWords(self, s: str) -> str:
        """Reverse order of words."""
        words = s.split(' ')
        words = [word for word in words if word != '']
        start, end = 0, len(words) - 1
        while start < end:
            words[start], words[end] = words[end], words[start]
            start += 1
            end -= 1
        return ''.join(f'{w} ' for w in words).strip()
# @lc code=end


def main():
    """Script main function."""
    s = Solution()

    words = 'the sky is blue'
    expected = 'blue is sky the'
    res = s.reverseWords(words)
    assert (res == expected)

    words = ' hello world '
    expected = 'world hello'
    res = s.reverseWords(words)
    assert (res == expected)

    words = 'a good  example'
    expected = 'example good a'
    res = s.reverseWords(words)
    assert (res == expected)

    print('Success')


if __name__ == '__main__':
    main()
