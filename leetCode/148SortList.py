# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if not head:
            return None
        tmpHead, count = head, 0
        while tmpHead:
            count += 1
            tmpHead = tmpHead.next
        res = self.mergeSortList(head, count)
        return res


    def mergeSortList(self, head, size):
        if size == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        leftSize = size/2
        rightSize = size-leftSize
        left, right = head, None
        slower, faster,prevSlower = head, head, dummy
        while faster.next and faster.next.next:
            slower, faster = slower.next, faster.next.next
            prevSlower = prevSlower.next
        if not faster.next:
            right = slower
            prevSlower.next = None
        elif faster.next and not faster.next.next:
            right = slower.next
            slower.next = None
        leftStart = self.mergeSortList(left, leftSize)
        rightStart = self.mergeSortList(right, rightSize)
        newHead = self. merge(leftStart, rightStart)
        return newHead


    def merge(self, left, right):
        dummy = ListNode(0)
        dummy.next = left
        prevLeft = dummy

        while right and left:
            if right.val <= left.val:
                newRight = right.next
                right.next = left
                prevLeft.next = right
                prevLeft = right
                right = newRight
            elif right.val > left.val:
                prevLeft = left
                left = left.next
                
        if not left:
            prevLeft.next = right
            
        return dummy.next

s = Solution()
a1, a2, a3, a4, a5 = ListNode(1),ListNode(2),ListNode(3),ListNode(4),ListNode(5)
a5.next, a4.next, a3.next, a2.next = a4, a3, a2, a1
res = s.sortList(a5)
while res:
    print res.val
    res = res.next

#check merge
s = Solution()
a1, a2, a3, a4, a5 = ListNode(1),ListNode(2),ListNode(3),ListNode(4),ListNode(5)
a1.next, a3.next = a3, a4
a2.next = a5
res = s.merge(a1, a2)

#check mergeSortList
a1, a2, a3, a4, a5 = ListNode(1),ListNode(2),ListNode(3),ListNode(4),ListNode(5)
a2.next = a1
a1.next = a3
res = s.mergeSortList(a2, 3)