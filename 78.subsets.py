#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if nums is None or len(nums) == 0:
            return []

        res = []
        self.getSubsets(nums, [], res)

        return res

    def getSubsets(self, nums: list[int], current: list[int], subsets: list[list[int]]):
        subsets.append(current[:])

        for i in range(len(nums)):
            current.append(nums[i])
            self.getSubsets(nums[i+1:], current, subsets)
            current.pop()

        return subsets
        
# @lc code=end

def main():
    s = Solution()

    nums = [1,2,3]
    res = s.subsets(nums)

    nums = [0]
    res = s.subsets(nums)

    return 0

if __name__ == '__main__':
    main()