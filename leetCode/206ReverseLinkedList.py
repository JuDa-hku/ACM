# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return 
        tmphead, tmpend = self.reverseListHelp(head)
        return tmphead


    def reverseListHelp(self, head):
        if head.next == None:
            return (head, head)
        else:
            tmpHead, tmpEnd = self.reverseListHelp(head.next)
            tmpEnd.next = head
            tmpEnd = tmpEnd.next
            tmpEnd.next = None
            return (tmpHead, tmpEnd)
            
a0, a1, a2 = ListNode(0), ListNode(1), ListNode(2)
a0.next = a1
a1.next = a2
s = Solution()
head = s.reverseList(a0)
while head:
    print head.val
    head = head.next
