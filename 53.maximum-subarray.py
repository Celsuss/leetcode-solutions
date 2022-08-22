#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        current_sum = max_sum

        for n in nums[1:]:
            if current_sum < 0:
                current_sum = 0

            current_sum += n
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum
        
# @lc code=end

def main():
    s = Solution()

    res = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    assert res == 6

    res = s.maxSubArray([1])
    assert res == 1

    res = s.maxSubArray([5,4,-1,7,8])
    assert res == 23

    return 0

if __name__ == '__main__':
    main()