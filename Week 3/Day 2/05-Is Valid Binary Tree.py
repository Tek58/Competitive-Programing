'''
Question -> https://leetcode.com/problems/validate-binary-search-tree/
@Author -> Taklemariam Alazar
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        result = []
        return self._helper(root, result)
        
    def _helper(self, root, result):
        if root is None:
            return 0
        self._helper(root.left, result)
        result.append(root.val)
        self._helper(root.right, result)
        
        for i in range(len(result)-1):
            if result[i] >= result[i+1]:
                return False
        return True