'''
Question -> https://leetcode.com/problems/minimum-depth-of-binary-tree/
@Author -> Taklemariam Alazar
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections.deque 
class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        queue = deque()
        queue.append(root)
        level = 1
        if (self.isLeaf(root)):
            return level
        while len(queue)!= 0:
            lenQueue = len(queue)
            for i in range(lenQueue):
                val = queue.popleft()
                if (not self.isLeaf(val)):
                    if val.left:
                        queue.append(val.left)
                    if val.right:
                        queue.append(val.right)
                else:
                    return level
            level += 1
        return level
        
    def isLeaf(self,root):
        if root.left is None and root.right is None:
            return True
