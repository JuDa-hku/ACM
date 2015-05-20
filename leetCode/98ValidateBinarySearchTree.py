# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        return self.inorderTraversal(root)
        
    # def inorderTraversal(self, root):
    #     res,tmpLeft,tmpRight = [],[],[]
    #     if not root:
    #         return []
    #     if root.left:
    #         tmpLeft = self.inorderTraversal(root.left)
    #     if root.right:
    #         tmpRight = self.inorderTraversal(root.right)
    #     res.extend(tmpLeft)
    #     res.append(root.val)
    #     res.extend(tmpRight)
    #     return res


            
    def inorderTraversal(self, root):
        res = []
        stack = []
        flag = True
        ptr = root
        if not root:
            return False
        while stack or ptr:
            if ptr:
                stack.append(ptr)
                ptr = ptr.left
            else:
                ptr = stack[-1]
                stack.pop()
                if flag:
                    current = ptr.val
                    flag = False
                else:
                    prev = current
                    current = ptr.val
                    if current<=prev:
                        return False
                ptr = ptr.right
        return True


a0, a1 = TreeNode(1), TreeNode(1)
a0.left = a1
s = Solution()
print s.isValidBST(None)