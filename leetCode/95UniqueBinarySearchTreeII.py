# Definition for a binary tree node.
import copy
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        nums = range(1,n+1,1)
        res = self.generateTreesHelp(nums)
        return res


    def generateTreesHelp(self, nums):
        res = []
        if len(nums) == 0:
            return [None]
        if len(nums) == 1:
            res.append(TreeNode(nums[0]))
            return res
        for i in xrange(len(nums)):
            numTreeNode = TreeNode(nums[i])
            tmpResLeft = self.generateTreesHelp(nums[:i])
            tmpResRight = self.generateTreesHelp(nums[i+1:])
            for left in tmpResLeft:
                for right in tmpResRight:
                    tmpRes = copy.deepcopy(numTreeNode)
                    tmpRes.left = left
                    tmpRes.right = right
                    res.append(tmpRes)
        return res

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
        
s= Solution()            
res = s.generateTrees(0)
for root in res:
    print s.inorderTraversal(root)