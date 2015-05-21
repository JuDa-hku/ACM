# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#recrusive
class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isSymmetricHelp(root.left, root.right)


    def isSymmetricHelp(self, p, q):
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        if p.val != q.val:
            return False
        else:
            return self.isSymmetricHelp(p.left, q.right) and self.isSymmetricHelp(p.right, q.left)


            
#iteratively
class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if not root:
            return True
        nodeStack = [root.left, root.right]
        while nodeStack:
            tmpRight = nodeStack.pop()
            tmpLeft = nodeStack.pop()
            if (not tmpRight and tmpLeft) or (not tmpLeft and tmpRight):
                return False
            elif not tmpRight and not tmpLeft:
                continue
            elif tmpRight.val!=tmpLeft.val:
                return False
            else:
                nodeStack.append(tmpRight.left)
                nodeStack.append(tmpLeft.right)
                nodeStack.append(tmpLeft.left)
                nodeStack.append(tmpRight.right)
        return True
            
            




            