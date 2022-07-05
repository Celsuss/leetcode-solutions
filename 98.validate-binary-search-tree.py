#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None or root.val is None:
            return False

        return self.confirmNode(root, -sys.maxsize, sys.maxsize)

    def confirmNode(self, node: Optional[TreeNode], minVal: int, maxVal: int) -> bool:
        if node.val <= minVal or node.val >= maxVal:
            return False

        if node.left is not None:
            if not self.confirmNode(node.left, minVal, node.val):
                return False
        if node.right is not None:
            return self.confirmNode(node.right, node.val, maxVal)
        
        return True
        
# @lc code=end

