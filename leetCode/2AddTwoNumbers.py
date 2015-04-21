# Definition for singly-linked list.
import copy
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        node = root = ListNode(0)
        n = 0
        while l1 and l2:
            value = n + l1.val + l2.val
            n, value = value/10, value%10
            nextNode = ListNode(value)
            node.next = nextNode
            node = node.next
            l1, l2 = l1.next, l2.next
        if l2:
            l1 = l2
        while l1:
            value = n + l1.val
            n, value = value/10, value%10
            nextNode = ListNode(value)
            node.next = nextNode
            node = node.next
            l1 = l1.next
        if n == 1:
            nextNode = ListNode(1)
            node.next = nextNode
        return root.next

x = [2, 4, 6, 1]
xNode = xNode1 = ListNode(0)
y = [5, 6, 4, 8, 9,9,9,9,9,9,]
yNode = yNode1 = ListNode(0)
for i in x:
   node = ListNode(i)
   xNode1.next = node
   xNode1 = xNode1.next
for i in y:
   node = ListNode(i)
   yNode1.next = node
   yNode1 = yNode1.next
s = Solution()
zNode = s.addTwoNumbers(xNode, yNode)
while zNode:
    print zNode.val
    zNode = zNode.next