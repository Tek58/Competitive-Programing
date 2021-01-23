'''
Question -> Maximum height of a BST
@Author Taklemariam Alazar
'''
def height(root):
    if root is None :
        return -1
    return max((height(root.left) + 1),(height(root.right) + 1))