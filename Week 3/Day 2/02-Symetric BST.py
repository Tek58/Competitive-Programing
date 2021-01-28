'''
Question -> https://leetcode.com/problems/symmetric-tree/submissions/
@Author -> Taklemariam Alazar
'''
def isSymmetric(self, root):
        if not root:
            return True
        return self._helper(root.right, root.left)
def _helper(self, leftTree,rightTree):
    if leftTree and not rightTree:
        return False
    elif rightTree and not leftTree:
        return False
    elif not rightTree and not leftTree:
        return True
    elif rightTree.val != leftTree.val:
        return False
    val1 = self._helper(rightTree.left, leftTree.right)
    val2 = self._helper(rightTree.right, leftTree.left)
    return val1 and val2