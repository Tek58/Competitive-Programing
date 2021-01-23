'''
Question -> https://leetcode.com/problems/range-sum-of-bst/
@Author -> Taklemariam Alazar
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(self, root: TreeNode, low: int, high: int):
        if root is None:
            return 0
        print(root.val)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low,high) 
        elif root.val >= low and root.val <= high:
            return root. val + self.rangeSumBST(root.right, low, high)  + self.rangeSumBST(root.left, low,high)