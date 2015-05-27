# Definition for binary tree with next pointer.
class TreeLinkNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         self.next = None
from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None
        while root:
            tmp = root
            stack = [tmp]
            sonStack = deque([])
            firstTag, nextRoot = True, None
            while stack:
                father = stack.pop()
                if father.left:
                    sonStack.append(father.left)
                if father.right:
                    sonStack.append(father.right)
                if father.next:
                    stack.append(father.next)
                if firstTag and sonStack:
                    firstTag = False
                    nextRoot = sonStack[0]
                while len(sonStack)>=2:
                    leftTmp = sonStack.popleft()
                    leftTmp.next = sonStack[0]
            root = nextRoot

a1, a2, a3, a4, a5, a7 = TreeLinkNode(1),TreeLinkNode(2),TreeLinkNode(3),TreeLinkNode(4),TreeLinkNode(5),TreeLinkNode(7)
a1.right, a3.right = a3, a7
a1.left, a2.left = a2, a4
a2.right = a5
s = Solution()
s.connect(a1)
