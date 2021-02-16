'''
Question -> https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
@Author -> Taklemariam alazar
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root):
        total_sum = [0]
        if not root:
            return 0
        if root.left:
            self._helper(root.left, root, total_sum)
        if root.right:
            self._helper(root.right, root, total_sum)
        return total_sum[0]
    
    def _helper(self, node, parent, total):
        
        if node.left and parent.val % 2 == 0: 
            total[0] += node.left.val
        
        if node.left:
            self._helper(node.left, node, total)
            
        if node.right and parent.val % 2 == 0:
            total[0] += node.right.val
        if node.right:
            self._helper(node.right, node, total)
            
        return total           