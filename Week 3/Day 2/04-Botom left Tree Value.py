'''
Question -> https://leetcode.com/problems/find-bottom-left-tree-value/
@Author -> Taklemariam Alazar
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # return 0
        # depth, value
        result = [-1, 0]
        self._helper(root, 0, result)
        return result[1]
    
    def _helper(self, root, curr_depth, res):
        if root is None:
            return 
        if curr_depth > res[0]:
            res[0], res[1] = curr_depth, root.val

        root.left = self._helper(root.left, curr_depth + 1, res) 
        root.right = self._helper(root.right, curr_depth + 1, res)