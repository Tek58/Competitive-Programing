'''
Question -> 
@Author -> Taklemariam Alazar
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def constructMaximumBinaryTree(self, nums):
        left = 0
        right = len(nums) - 1
        return self._helper(nums,left,right)
def _helper(self,nums, left, right):
    if left > right:
        return
    Max = -1
    index_max = 0
    for i in range(left, right+1):
        if Max < nums[i]:
            Max = nums[i]
            index_max = i
    root = TreeNode(Max)
    root.left = self._helper(nums,left, index_max-1)
    root.right = self._helper(nums,index_max + 1,right)
    return root