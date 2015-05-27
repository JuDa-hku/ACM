# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
from collections import deque
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if not root:
            return 0
        stack = deque([(root, 1)])
        while stack:
            tmp = stack.popleft()
            if not tmp[0].right and not tmp[0].left:
                return tmp[1]
            if tmp[0].right:
                stack.append((tmp[0].right, tmp[1]+1))
            if tmp[0].left:
                stack.append((tmp[0].left, tmp[1]+1))


a0 = TreeNode(0)
a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(2)
a0.left, a0.right = a1, a2
a2.right = a3
s = Solution()
print s.minDepth(a0)