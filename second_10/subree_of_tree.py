class Solution(object):
    def rt(self,root,n):
        if root == None:
            return None
        if root.val == n:
            return root
        if self.rt(root.left,n) != None:
            return self.rt(root.left,n)
        if self.rt(root.right,n) != None:
            return self.rt(root.right,n)
        return False
    def isSubtree(self, root, subRoot):
