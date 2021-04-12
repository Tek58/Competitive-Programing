'''
Question -> https://leetcode.com/problems/path-sum/
@Author -> Taklemariam Alazar
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, node: TreeNode, targetSum: int) -> bool:
        if not node:
            return False
        if node.left is None and  node.right is None:
            return targetSum == node.val

        return self.hasPathSum(node.left,targetSum-node.val) or self.hasPathSum(node.right, targetSum-node.val)