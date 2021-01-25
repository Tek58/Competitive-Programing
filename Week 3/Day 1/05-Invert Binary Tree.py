'''
Question -> https://leetcode.com/problems/invert-binary-tree/
@Author -> Taklemariam Alazar
'''
def isSameTree(self, p, q):
        if p is None and q is None :
            return True
        if p is not None and q is None:
            return False
        if q is not None and p is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right,q.right ) and self.isSameTree(p.left, q.left) 