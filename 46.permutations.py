#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums[:]]

        out = []
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            nums.append(n)

            out.extend(perms)

        return out
        
# @lc code=end

def main():
    s = Solution()

    nums = [1, 2, 3]
    out = s.permute(nums)
    assert(len(out) == 3*2*1)

    nums = [0, 1]
    out = s.permute(nums)
    assert(len(out) == 1*2)

    nums = [1]
    out = s.permute(nums)
    assert(out == [[1]])

    return 0

if __name__ == '__main__':
    main()