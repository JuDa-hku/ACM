# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def calculateHeight(self, root):
        if root == None:
            return 0
        if root.right == None and root.left==None:
            return 1
        height = max(self.calculateHeight(root.right), self.calculateHeight(root.left)) + 1
        return height
        
    def checkOne(self, root):
        value = self.calculateHeight(root.right)-self.calculateHeight(root.left)
        if value==-1 or value == 1 or value==0:
            return True
        else:
            return False
        
    def isBalanced(self, root):
        if root == None:
            return True
        if root.right == None and root.left == None:
            return True
        if not self.checkOne(root):
            return False
        result = self.isBalanced(root.left) and self.isBalanced(root.right)
        return result
        
s = Solution()
a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a1.left = a2
# a2.left = a3
# a3.left = a5
a1.right = a4

print s.isBalanced(a1)