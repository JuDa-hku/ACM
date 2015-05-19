# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        if not head or not head.next:
            return head
        dummyHead =  ListNode(0)
        dummyHead.next = head
        start, end = dummyHead, head
        if end.val<x:
            start = end
        head = head.next
#        print head.val
        while head:
            newhead = head.next
#            print head.val, x, end.val
            if head.val<x and x<=end.val:
                head.next = start.next
                start.next = head
                start = head
            elif head.val<x and x>end.val:
                end.next = head
                start = end.next
                end = head
                head.next = None
            elif head.val>=x:
                end.next = head
                head.next = None
                end = head
            head = newhead
        end.next = None
        return dummyHead.next





           
a0, a1, a2, a3, a4 = ListNode(2), ListNode(4),ListNode(1), ListNode(3), ListNode(4)
b0 = ListNode(0)
a0.next = b0
b0.next = a1
a1.next = a2
a2.next = a3
a3.next = a4
s = Solution()
newHead = s.partition(a0,4)
while newHead:
    print newHead.val
    newHead = newHead.next
                
            