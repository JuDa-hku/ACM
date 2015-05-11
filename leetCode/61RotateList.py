# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        length, tmpNode = 1, head
        if not head:
            return None
        while tmpNode.next:
            tmpNode = tmpNode.next
            length += 1
#        print length, k
        k = k%length
        if k==0:
            return head
        ##tmpNode is the last node
        i = 1
        endNode, tmp = tmpNode, head
        while i<length-k:
            i += 1
            tmp = tmp.next
        newHead = tmp.next
        tmp.next = None
        endNode.next = head
        return newHead
        
        
head = ListNode(1)
node2 = ListNode(2)        
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
#head.next = node2
#node2.next = node3
node3.next = node4
node4.next = node5
s = Solution()
head = None
newHead = s.rotateRight(head,1)