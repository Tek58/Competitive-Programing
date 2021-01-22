'''
Question ->  https://leetcode.com/problems/search-in-a-binary-search-tree/
@Author -> Taklemariam Alazar
'''
def searchBST(self, root, val):
    if root is None:
        return 
    if root.val  == val:
        return root
    
    if val <= root.val:
        return self.searchBST(root.left, val)
    elif val > root.val:
        return self.searchBST(root.right, val)