# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if not root:
            return 0
        nodeStack = deque([(root,1)])
        res = 0
        while nodeStack:
            considered = nodeStack.pop()
            index = considered[1]
            node = considered[0]
            if node.right:
                nodeStack.append((node.right, index+1))
            if node.left:
                nodeStack.append((node.left, index+1))
            if index>=res:
                res = index
        return res
