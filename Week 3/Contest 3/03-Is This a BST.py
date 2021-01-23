'''
Question -> Checking for BST
@Author -> Taklemariam Alazar
'''

val = []
def check_binary_search_tree_(root):
    if root is None:
        return 0
    check_binary_search_tree_(root.left)
    val.append(root.data)
    check_binary_search_tree_(root.right)
    for i in range(len(val)-1):
        if val[i] >= val[i+1]:
            return False
    return True