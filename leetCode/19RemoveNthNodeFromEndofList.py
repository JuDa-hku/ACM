# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
from collections import deque
class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        nodeDe = deque()
        dummy = head
        if n == 1 and not head.next:
            return None
        while head:
            nodeDe.append(head)
            if len(nodeDe) == n+2:
                nodeDe.popleft()
            head = head.next
        if n == 1:
            nodeDe[-2].next = None
        elif len(nodeDe) <= n:
            return dummy.next
        else:
            nodeDe[0].next = nodeDe[2]
        return dummy

a0 = ListNode(0)
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a0.next = a1
a1.next = a2
a2.next = a3
a3.next =a4
s= Solution()
newa = s.removeNthFromEnd(a0, 2)
while newa:
    print newa.val
    newa = newa.next


