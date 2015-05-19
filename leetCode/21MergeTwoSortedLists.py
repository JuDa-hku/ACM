# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        newHead = dummy
        while l1 and l2:
            if l1.val<=l2.val:
                newHead.next = l1
                newHead = l1
                l1 = l1.next
            else:
                newHead.next = l2
                newHead = l2
                l2 = l2.next
        if l1:
            newHead.next = l1
        if l2:
            newHead.next = l2
        return dummy.next

