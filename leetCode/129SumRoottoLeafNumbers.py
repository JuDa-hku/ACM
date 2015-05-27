# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        stack = [root]
        res = 0
        if not root:
            return 0
        while stack:
            nodeCon = stack[-1]
            if nodeCon.left:
                nodeCon.left.val += 10*nodeCon.val
                stack.append(nodeCon.left)
            elif nodeCon.right:
                nodeCon.right.val += 10*nodeCon.val
                stack.pop()
                stack.append(nodeCon.right)
            elif not nodeCon.left and not nodeCon.right:
                res += nodeCon.val
                stack.pop()
                while stack:
                    fatherNode = stack.pop()
                    if fatherNode.right:
                        fatherNode.right.val += fatherNode.val*10
                        stack.append(fatherNode.right)
                        break
                        
        return res
a1, a2, a3, a4 = TreeNode(1),TreeNode(2),TreeNode(3),TreeNode(4)
a1.left,a2.left, a3.left = a2, a3,a4
#a1.left = a2
s = Solution()
print s.sumNumbers(a1)