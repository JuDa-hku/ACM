# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        dummyStart = dummy
        count = 0
        if m == n:
            return head
        while True:
            if count == m-1:
                startRotate = dummyStart
            if count == n:
                endRotate = dummyStart
                break
            dummyStart = dummyStart.next
            count += 1
        if not endRotate.next:
            tmphead, tmpend = self.reverseList(startRotate.next)
            startRotate.next = tmphead
            return dummy.next
        if endRotate:
            endRotateAfter = endRotate.next
            endRotate.next = None
            tmphead, tmpend = self.reverseList(startRotate.next)
            startRotate.next = tmphead
            tmpend.next = endRotateAfter
            return dummy.next
 
    def reverseList(self, head):
        if not head:
            return 
        tmphead, tmpend = self.reverseListHelp(head)
        return tmphead, tmpend


    def reverseListHelp(self, head):
        if head.next == None:
            return (head, head)
        else:
            tmpHead, tmpEnd = self.reverseListHelp(head.next)
            tmpEnd.next = head
            tmpEnd = tmpEnd.next
            tmpEnd.next = None
            return (tmpHead, tmpEnd)


            
a0, a1, a2,a3,a4 = ListNode(0), ListNode(1), ListNode(2),ListNode(3), ListNode(4)
#a0.next = a1
a1.next = a2
a2.next = a3
a3.next = a4
s = Solution()
head = s.reverseBetween(a0,1,1)
while head:
    print head.val
    head = head.next
