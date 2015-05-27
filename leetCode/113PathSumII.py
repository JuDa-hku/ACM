# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class NodeSum:
    def __init__(self, node, sum, path):
        self.node = node
        self.sum = sum
        self.path = path

from collections import deque
class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        stack = deque([NodeSum(root, sum, [])])
        res = []
        if not root:
            return []
        while stack:
            con = stack.popleft()
            if con.node.right:
                rootRight = con.node.right
                sumRight = con.sum-con.node.val
#                print con.path
                path = con.path[::1]
                path.append(con.node.val)
                stack.append(NodeSum(rootRight, sumRight, path))
            if con.node.left:
                rootLeft = con.node.left
                sumLeft = con.sum-con.node.val
                path = con.path[::1]
                path.append(con.node.val)
                stack.append(NodeSum(rootLeft, sumLeft, path))
            if not con.node.right and not con.node.left and con.sum == con.node.val:
                tmpPath = con.path[::1]
                tmpPath.append(con.node.val)
                res.append(tmpPath)
        return res



node5, node4, node8, node11, node13, node40, node7, node2, node50, node1 = TreeNode(5),TreeNode(4),TreeNode(8),TreeNode(11),TreeNode(13),TreeNode(4),TreeNode(7),TreeNode(2),TreeNode(5),TreeNode(1)
node5.right,node8.right,node40.right = node8, node40, node1
node5.left, node4.left,node11.left = node4, node11, node7
node11.right = node2
node8.left = node13
node40.left = node50
s = Solution()
print s.pathSum(node5,22)
