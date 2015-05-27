# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
from collections import deque
class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        if len(postorder) == 0:
            return None
        inorder = deque(inorder[::-1])
        postorder = deque(postorder[::-1])
        root = TreeNode(postorder.popleft())
        stackNode = [root]
        while inorder and stackNode and postorder:
            tmpNode = stackNode[-1]
            t = []
            for i in stackNode:
                t.append(i.val)
 #           print t, inorder
            if inorder[0] != tmpNode.val:
                node = TreeNode(postorder.popleft())
                tmpNode.right = node
                stackNode.append(node)

            elif inorder[0] == tmpNode.val:
                stackNode.pop()
                inorder.popleft()
                if stackNode and inorder:
                    if stackNode[-1].val == inorder[0]:
                        continue
                    if stackNode[-1].val != inorder[0]:
                        tmpNode.left = TreeNode(postorder.popleft())
                        stackNode.append(tmpNode.left)
                elif not stackNode and inorder:
                    tmpNode.left = TreeNode(postorder.popleft())
                    stackNode.append(tmpNode.left)
        return root

s = Solution()
root =s.buildTree([5,3,6,2,7,4,8],[5,6,3,7,8,4,2])