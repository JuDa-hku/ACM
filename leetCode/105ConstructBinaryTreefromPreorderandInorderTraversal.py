# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        i0, j0 = 0, 0
        i1, j1 = len(preorder), len(inorder)
        root = self.buildTreeHelp(preorder, inorder, i0, i1, j0, j1)
        return root

    
    def buildTreeHelp(self, preorder, inorder, i0, i1, j0, j1):
#        print i0, i1, j0, j1
        if not preorder[i0:i1] or not inorder[j0:j1]:
            return None
        if len(preorder[i0:i1]) == 1:
            return TreeNode(preorder[i0])
        root = TreeNode(preorder[i0])
        ##search the position of root in inorder to define the left tree
        i = inorder.index(preorder[i0])
        leftNode = self.buildTreeHelp(preorder, inorder, i0+1, i-j0+i0+1, j0, i)
        rightNode = self.buildTreeHelp(preorder, inorder, i1+1+i-j1, i1, i+1, j1)
        root.left = leftNode
        root.right = rightNode
        return root



##iterative
from collections import deque
class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        preorder, inorder = deque(preorder), deque(inorder)
        root = TreeNode(preorder.popleft())
        stackNode = [root]
        while stackNode and inorder:
            tmpNode = stackNode[-1]
            #go to left
#            print tmpNode.val, preorder, inorder
            if tmpNode.val == inorder[0]:
                inorder.popleft()
                stackNode.pop()
                if inorder and not stackNode:
                    tmpNode.right = TreeNode(preorder.popleft())
                    stackNode.append(tmpNode.right)
                elif inorder and stackNode:
                    if stackNode[-1].val != inorder[0]:
                        tmpNode.right = TreeNode(preorder.popleft())
                        stackNode.append(tmpNode.right)
            
            elif tmpNode.val!=inorder[0]:
                if preorder:
                    numPreOrderNode = TreeNode(preorder.popleft())
                    tmpNode.left = numPreOrderNode
                    stackNode.append(numPreOrderNode)
        return root

            

            
            
            
                

s = Solution()

root = s.buildTree([1,2,3],[1,3,2])
#root = s.buildTree([2,3,5,6,4],[5,3,6,2,4])

