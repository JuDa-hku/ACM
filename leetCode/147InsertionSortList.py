# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return None
        curr = head.next
        startCurr, endCurr = head, head
        while curr!=None:
            nextCurr = curr.next
            if curr.val<=startCurr.val:
                endCurr.next = curr.next
                curr.next = startCurr
                startCurr = curr
            elif curr.val>=endCurr.val:
                endCurr = curr
            else:
                tmp = startCurr
                while tmp.next.val<curr.val:
                        tmp = tmp.next
                endCurr.next = curr.next
                curr.next = tmp.next
                tmp.next = curr
            curr = nextCurr
        return startCurr

a1,a2,a3,a4 = ListNode(1),ListNode(2),ListNode(3),ListNode(4)
a2.next, a4.next,a1.next = a4, a1, a3
s = Solution()
b = s.insertionSortList(a2)