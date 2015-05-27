# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
from collections import deque         
class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        if not root:
            return None
        stack = [root]
        stackLeft = deque([])
        stackRight = []
        if root.left:
            stackLeft.append(root.left)
        if root.right:
            stackRight.append(root.right)
            
        while stack:
            tmp = stack.pop()
            if stackLeft:
                tmpLeft = stackLeft.popleft()
                tmp.right = tmpLeft
                tmp.left = None
                stack.append(tmpLeft)
                if  tmpLeft.left:
                    stackLeft.append(tmpLeft.left)
                if  tmpLeft.right:
                    stackRight.append(tmpLeft.right)
            else:
                if not stackRight:
                    return
                tmpRight = stackRight.pop()
                tmp.right = tmpRight
                stack.append(tmpRight)
                if  tmpRight.left:
                    stackLeft.append(tmpRight.left)
                if  tmpRight.right:
                    stackRight.append(tmpRight.right)

            
        
                
        



n1, n2, n3, n4, n5, n6 = TreeNode(1),TreeNode(2),TreeNode(3),TreeNode(4),TreeNode(5),TreeNode(6)
n1.right,n5.right = n5, n6
n1.left, n2.left = n2, n3
n2.right = n4
s = Solution()
s.flatten(n2)
