# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return None
        dummy = ListNode(0)
        newHead, value, appendFlag = dummy, head.val, True
        while head.next:
            if head.next.val != value:
                if appendFlag:
                    newHead.next = head
                    newHead = newHead.next
                head = head.next
                value = head.val
                appendFlag = True
#                print "value",value
            elif head.next.val == value:
                head = head.next
                appendFlag = True
## to handle the end                
        if appendFlag:
            newHead.next = head
            newHead = newHead.next
        newHead.next = None
        return dummy.next


           
a0, a1, a2, a3, a4 = ListNode(0), ListNode(1),ListNode(2), ListNode(2), ListNode(4)
b0 = ListNode(0)
a0.next = b0
b0.next = a1
a1.next = a2
a2.next = a3
a3.next = a4
s = Solution()
newHead = s.deleteDuplicates(a0)
while newHead:
    print newHead.val
    newHead = newHead.next