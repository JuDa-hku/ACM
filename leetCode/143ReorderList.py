# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
from collections import deque
class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        stack = deque([])
        while head:
            stack.append(head)
            head = head.next
        left, lastRight,right = None, None, None
        while stack:
            left = stack.popleft()
            if lastRight:
                lastRight.next = left
            if stack:
                right = stack.pop()
                left.next = right
                lastRight = right
                if not stack:
                    right.next = None
            elif not stack:
                left.next = None
                

a0 = ListNode(0)
a1 = ListNode(1)
a2 = ListNode(2)
#a3 = ListNode(3)
a0.next, a1.next, a2.next = a1, a2, None
s = Solution()
s.reorderList(a0)