#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        start_index = -1
        end_index = -1

        def divideAndConquer(nums: list[int], nums_start_index=0):
            nonlocal start_index, end_index
            if len(nums) == 0:
                return 0

            if len(nums) == 1 and nums[0] == target:
                if start_index == -1:
                    start_index = nums_start_index
                else:
                    end_index = nums_start_index
                return 0
            elif len(nums) == 1:
                return 0

            split_index = int(len(nums)/2)

            # Split list in two
            l_nums = nums[:split_index]
            r_nums = nums[split_index:]

            # Find which sub list has our targets
            if len(l_nums) > 0 and target <= l_nums[-1]:
                # Target is in l_nums
                divideAndConquer(l_nums, nums_start_index)
            if len(r_nums) > 0 and target >= r_nums[0]:
                # Target is in r_nums
                divideAndConquer(r_nums, nums_start_index+split_index)

            return 0

        res = divideAndConquer(nums)
        if start_index != -1 and end_index == -1:
            end_index = start_index
        return [start_index, end_index]
        
# @lc code=end

def main():
    s = Solution()

    nums = [1,2,3,3,3,3,4,5,9]
    target = 3
    res = s.searchRange(nums, target)
    assert(res == [2, 5])

    nums = [5,7,7,8,8,10]
    target = 8
    res = s.searchRange(nums, target)
    assert(res == [3,4])

    nums = [5,7,7,8,8,10]
    target = 6
    res = s.searchRange(nums, target)
    assert(res == [-1,-1])

    nums = []
    target = 0
    res = s.searchRange(nums, target)
    assert(res == [-1,-1])

    return

if __name__ == '__main__':
    main()