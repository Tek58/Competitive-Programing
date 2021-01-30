'''
Question -> Postorder traversal of BST 
@Author -> Taklemariam Alazar
'''
def postorderTraversal(self, root):
        result = []
        return self.helper(root,result)
        
def helper(self, root, result):
    if root is None:
        return 
    self.helper(root.left, result)
    self.helper(root.right, result)
    result.append(root.val)
    return result