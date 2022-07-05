#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None or root.val is None:
            return False

        current_sum = 0
        leafSum = self.getSum(root, current_sum, targetSum)
        return leafSum == targetSum

    def getSum(self, node: Optional[TreeNode], currentSum: int, targetSum: int) -> int:
        currentSum += node.val

        if node.left is not None and node.left.val is not None:
            leafSum = self.getSum(node.left, currentSum, targetSum)
            if leafSum == targetSum:
                return leafSum

        if node.right is not None and node.right.val is not None:
            return self.getSum(node.right, currentSum, targetSum)

        return currentSum if node.right is None and node.left is None else targetSum-1
        
# @lc code=end

