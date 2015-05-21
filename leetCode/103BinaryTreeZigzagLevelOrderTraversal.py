# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        nodeStack = deque([(root,0)])
        res = []
        while nodeStack:
            considered = nodeStack.pop()
            index = considered[1]
            node = considered[0]
            if node.right:
                nodeStack.append((node.right, index+1))
            if node.left:
                nodeStack.append((node.left, index+1))
            if index<len(res):
                if index%2 == 0:
                    res[index].append(node.val)
                if index%2 == 1:
                    res[index].insert(0, node.val)
            elif index>=len(res):
                res.append([node.val])
        return res