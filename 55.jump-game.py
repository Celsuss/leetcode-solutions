#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start

class Node:
    def __init__(self, val, index):
        self.val = val
        self.index = index

class Solution:
    def canJump(self, nums) -> bool:
        if len(nums) == 1 or len(nums) == 0 or all(x != 0 for x in nums):
            return True

        investigated = []
        return self.getNextNode(len(nums)-1, nums, investigated)

    def getNextNode(self, index, nums, investigated):
        # print('Node val: {}, index: {}'.format(nums[index], index))
        if index == 0:
            return True

        for i in reversed(range(index)):
            if i + nums[i] >= index and i not in investigated:
                investigated.append(index)
                if self.getNextNode(i, nums, investigated) is True:
                    return True
        
        return False
        
# @lc code=end

if __name__ == '__main__':
    s = Solution()

    test_input = [4,3,2,1,0]
    res = s.canJump(test_input)
    assert res == True
    print()

    test_input = [1,2,3,4]
    res = s.canJump(test_input)
    assert res == True
    print()

    test_input = [2,3,1,1,4]
    res = s.canJump(test_input)
    assert res == True
    print()

    test_input = [3,0,8,2,0,0,1]
    res = s.canJump(test_input)
    assert res == True
    print()

    test_input = [3,2,1,0,4]
    res = s.canJump(test_input)
    assert res == False
    print()

    test_input = [0,2,3]
    res = s.canJump(test_input)
    assert res == False