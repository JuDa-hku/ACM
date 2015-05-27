# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None
        while root:
            tmp = root
            if tmp.left:
                while tmp:
                    tmp.left.next = tmp.right
                    if tmp.next:
                        tmp.right.next = tmp.next.left
                    tmp = tmp.next
            root = root.left

    
                