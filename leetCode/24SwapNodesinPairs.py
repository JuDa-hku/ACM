# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
import copy
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if head == None:
            return head
        if head.next == None:
            return head
        nextNode = head.next            
        tmpHead = self.swapPairs(nextNode.next)
        head.next = tmpHead
        nextNode.next = head
        return nextNode

s = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b; b.next = c; c.next=d
newa = s.swapPairs(a)