#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height) -> int:
        area = 0
        n = len(height)
        l = 0
        r = n-1

        while l < r:
            hl = height[l]
            hr = height[r]
            area = max(area, self.getArea(l, hl, r, hr))
            if hl < hr:
                l += 1
            else:
                r -= 1

        return area

    def getArea(self, x1, y1, x2, y2):
        y = y1 if y1 < y2 else y2
        x = x2-x1
        return x * y
        
# @lc code=end

def main():
    s = Solution()

    x = [1, 2, 3, 4]
    y = s.maxArea(x)
    assert(y == 4)

    x = [1,1]
    y = s.maxArea(x)
    assert(y == 1)

    x = [1,8,6,2,5,4,8,3,7]
    y = s.maxArea(x)
    assert(y == 49)
    
    return 0

if __name__ == '__main__':
    main()