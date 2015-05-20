# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def recoverTree(self, root):
        first, second = self.morrisTraversal(root)
        first.val, second.val = second.val, first.val

    def morrisTraversal(self, root):
        curr = root
        previous = None
        first, second, prev = None, None, None
#        res = []
        while curr:
            if not curr.left:
#                res.append[curr.val]
                if previous:
                    if previous.val>curr.val and not first:
                        first, second = previous, curr
                    elif previous.val>curr.val and first:
                        second = curr
                previous = curr
                curr = curr.right
            else:
                prev = curr.left
                while  prev.right and prev.right != curr:
                    prev = prev.right
                if not prev.right:
                    prev.right = curr
                    curr = curr.left
                elif prev.right == curr:
                    prev.right = None
#                    res.append[curr.val]
                    previous = prev
                    if previous.val>curr.val and not first:
                        first, second = previous, curr
                    elif previous.val>curr.val and first:
                        second = curr
                    previous = curr
                    curr = curr.right
        return first,second
    
                
a0, a1,a2,a3= TreeNode(0), TreeNode(1), TreeNode(0), TreeNode(3)
a1.right = a2
#a2.right = a3
#a1.left = a0
s = Solution()
s.recoverTree(a1)
