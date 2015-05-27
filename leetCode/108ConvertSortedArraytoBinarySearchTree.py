# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST1(self, nums):
        if len(nums) == 0:
            return None
        n = len(nums)
        if n == 1:
            return TreeNode(nums[0])
        middle = n/2
        root = TreeNode(nums[middle])
        leftNode = self.sortedArrayToBST(nums[:middle])
        rightNode = self.sortedArrayToBST(nums[middle+1:])
        root.left = leftNode
        root.right = rightNode
        return root

    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        n = len(nums)
        if n == 1:
            return TreeNode(nums[0])
        head = TreeNode(0)
        nodeStack = [head]
        leftStack = [0]
        rightStack = [n-1]
        while nodeStack:
            node = nodeStack.pop()
            leftIndex, rightIndex = leftStack.pop(), rightStack.pop()
            middle = leftIndex + (rightIndex-leftIndex)/2
            node.val = nums[middle]
            if leftIndex<middle:
                leftStack.append(leftIndex)
                rightStack.append(middle-1)
                leftTreeNode = TreeNode(0)
                node.left = leftTreeNode
                nodeStack.append(leftTreeNode)
            if middle<rightIndex:
                leftStack.append(middle+1)
                rightStack.append(rightIndex)
                rightTreeNode = TreeNode(0)
                node.right = rightTreeNode
                nodeStack.append(rightTreeNode)
        return head
                
                
            
            

            
            


                
        
s = Solution()            
root = s.sortedArrayToBST(range(2))
                
        

        