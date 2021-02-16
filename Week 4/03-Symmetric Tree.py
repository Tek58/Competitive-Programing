'''
Question -> https://leetcode.com/problems/symmetric-tree/
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
    def isSymmetric(self, root):
        queue = deque()
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if ((root.left) and (not root.right)) or ((root.right) and (not root.left)):
            return False
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            lenQueue = len(queue)
            for i in range(lenQueue//2):
                val1 = queue.popleft()
                val2 = queue.popleft()
                if (val1.val == val2.val):
                    if (self.isLeaf(val1) and self.isLeaf(val2) and len(queue)==0):
                        return True
                    elif (val1.left and val1.right) and (val2.left and val2.right):
                        queue.append(val1.left)
                        queue.append(val2.right)
                        queue.append(val1.right)
                        queue.append(val2.left)
                    else:
                        if ((val1.left and val2.right) and ((not val1.right) and (not val2.left))):
                            queue.append(val1.left)
                            queue.append(val2.right)
                        elif ((val1.right and val2.left) and ((not val1.left) and (not val2.right))):
                            queue.append(val1.right)
                            queue.append(val2.left)
                        else:
                            if (val1.left and val2.left) or (val1.right and val2.right):
                                return False
                            if len(queue) == 0:
                                return False
                else:
                    return False
        return False             
                
    def isLeaf(self, root):
        if (not root.left and not root.right):
            return True
        return False           