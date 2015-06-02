# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        tmpHeadA, tmpHeadB = headA, headB
        lengthA, lengthB, lastA, lastB = 1, 1, headA, headB
        while tmpHeadA.next:
            lengthA += 1
            tmpHeadA = tmpHeadA.next
        lastA = tmpHeadA
        while tmpHeadB.next:
            lengthB += 1
            tmpHeadB = tmpHeadB.next
        lastB = tmpHeadB
        if lastA != lastB:
            return None

        if lengthA>lengthB:
            for i in xrange(lengthA-lengthB):
                headA = headA.next
        else:
            for i in xrange(lengthB-lengthA):
                headB = headB.next

        while headA != headB:
            headA, headB = headA.next, headB.next

        return headA


    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        ptA, ptB, jumpA = headA, headB, False
        while True:
            if id(ptA) == id(ptB):
                return ptA
            ptA, ptB = ptA.next, ptB.next
            if not ptA:
                if not jumpA:
                    jumpA = True
                    ptA = headB
                else:
                    return None
            if not ptB:
                ptB = headA

        