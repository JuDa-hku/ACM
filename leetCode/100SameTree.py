# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        if q.val == p.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
        if q.val != p.val:
            return False