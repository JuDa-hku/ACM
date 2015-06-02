# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
#return the root first
from collections import deque
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        if not root:
            return []
        stack = deque([root])
        res = []
        while stack:
            tmp = stack.popleft()
            res.append(tmp.val)
            if tmp.right:
                stack.appendleft(tmp.right)
            if tmp.left:
                stack.appendleft(tmp.left)
        return res

a0, a1, a2, a3, a4 = TreeNode(0), TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4),
a0.left = a1
a0.right = a2
a1.left, a1.right = a3, a4
s = Solution()
print s.preorderTraversal(a0)

            
        