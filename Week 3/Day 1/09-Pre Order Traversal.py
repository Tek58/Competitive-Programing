'''
Question -> Binary Pre Order traversal
@Author -> Taklemariam Alazar
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def preorderTraversal(self, root):
        result = []
        return self.helper(root,result)
        
def helper(self, root, result):
    if root is None:
        return 
    result.append(root.val)
    self.helper(root.left, result)
    self.helper(root.right, result)
    
    return result
# Itrative Aproach
def preorderTraversalItretive(self, root: TreeNode) :
        result = []
        stack = [root]  
        while len(stack) > 0:
            value = stack.pop()
            if value:
                result.append(value.val)
                stack.append(value.right)
                stack.append(value.left)
        return result

# def postorderTraversalItretive(self, root: TreeNode) :
#         result = []
#         stack = []  
#         while len(stack) > 0:
#             value = stack.pop()
#             if value:
#                 result.append(value.val)
#                 stack.append(value.right)
#                 stack.append(value.left)
#         return result