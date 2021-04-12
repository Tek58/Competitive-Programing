'''
Question -> https://leetcode.com/contest/weekly-contest-174/problems/maximum-product-of-splitted-binary-tree/
@Author -> Taklemariam Alazar
'''
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        memo = {}
        totalSum = self.totalSumFinder(root, memo)
        return max([edge * (totalSum - edge) for edge in memo.values()]) % (10**9 +7)
    
    def totalSumFinder(self, root, memo):
        memo[root] = total = root.val + self.totalSumFinder(root.left, memo) + self.totalSumFinder(root.right, memo) if root else 0
        return total
        