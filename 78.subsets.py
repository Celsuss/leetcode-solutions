#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return None

        res = []
        self.getSubsets(nums, 0, [], res)
        # subsets = self.backPropegate(nums)

        return res

    def getSubsets(self, nums: list[int], start: int, current: list[int], subsets: list[list[int]]):
        subsets.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            self.getSubsets(nums, i+1, current, subsets)
            current.pop()

            continue

        return subsets

    def backPropegate(self, nums: list[int]) -> list[list[int]]:
        if len(nums) <= 1:
            return None

        subsets = []
        # Backpropegate by removing one element at a time
        for i in range(len(nums)):
            new_set = [nums[j] for j in range(len(nums)) if j != i]
            subsets.append(new_set)

            new_sets = self.backPropegate(new_set)
            if new_sets is None:
                continue

            for i in range(len(new_sets)):
                subsets.append(new_sets[i])

            continue

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