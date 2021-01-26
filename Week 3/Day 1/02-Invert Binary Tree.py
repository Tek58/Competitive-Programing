'''
Question -> https://leetcode.com/problems/invert-binary-tree/
@Author -> Taklemariam Alazar
'''
def invertTree(self, root):
        if root is None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

