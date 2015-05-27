# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        if not head:
            return None
        count = 0
        tmp = head
        while head:
            count += 1
            head = head.next
        return self.sortedListToBSTHelp(count, [tmp])

    def sortedListToBSTHelp(self, length, currRoot):
        if length == 0:
            return None
        if length == 1:
            node = TreeNode(currRoot[0].val)
            currRoot[0] = currRoot[0].next
            return node
        else:
            middle = length/2
            left = self.sortedListToBSTHelp(middle, currRoot)
            node = TreeNode(currRoot[0].val)
            currRoot[0] = currRoot[0].next
            right = self.sortedListToBSTHelp(length-middle-1, currRoot)
            node.left = left
            node.right = right
            return node

            
s = Solution()        
a0, a1,a2 = ListNode(0), ListNode(1), ListNode(2)
a0.next, a1.next = a1, a2
res =  s.sortedListToBST(a2)
        