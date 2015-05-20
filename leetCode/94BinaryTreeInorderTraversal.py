# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        res,tmpLeft,tmpRight = [],[],[]
        if not root:
            return []
        if root.left:
            tmpLeft = self.inorderTraversal(root.left)
        if root.right:
            tmpRight = self.inorderTraversal(root.right)
        res.extend(tmpLeft)
        res.append(root.val)
        res.extend(tmpRight)
        return res

node1, node2, node3 = TreeNode(1), TreeNode(2), TreeNode(3)
node1.right = node2
node2.left = node3
s = Solution()
print s.inorderTraversal(node1)