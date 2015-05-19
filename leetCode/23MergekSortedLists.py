# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            middle = (len(lists)/2)
            tmp1 = self.mergeKLists(lists[:middle])
            tmp2 = self.mergeKLists(lists[middle:])
            return self.mergeTwoLists(tmp1, tmp2)

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

