# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
#        self.node = root
        self.nodeValue = []
        tmpNodeStack = []
        tmpNode = None
        if not root:
            tmpNode = None
        elif root:
            tmpNode = root

        while tmpNodeStack or tmpNode:
            while tmpNode:
                tmpNodeStack.append(tmpNode)
                tmpNode = tmpNode.right
                
            if tmpNodeStack:
                tmpNode = tmpNodeStack.pop()
                self.nodeValue.append(tmpNode.val)
                tmpNode = tmpNode.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.nodeValue:
            return True
        return False
        
    # @return an integer, the next smallest number
    def next(self):
        if self.hasNext():
            return self.nodeValue.pop()
        

# Your BSTIterator will be called like this:


root,r4, r3, r2, r1, r0 = TreeNode(5), TreeNode(4),TreeNode(3),TreeNode(2),TreeNode(1),TreeNode(0)
root.left = r3
r3.left, r2.left, r1.left = r2, r1, r0
r3.right = r4
i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())