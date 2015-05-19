# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        tmpNodeList, resflag, res = [], True, head
        if not head:
            return None
        while head:
            tmpNodeList.append(head)
            head = head.next
            if len(tmpNodeList) == k:
                res = tmpNodeList[-1]
                for i in xrange(k-1,0,-1):
                    tmpNodeList[i].next = tmpNodeList[i-1]
                tmpNodeList[0].next = self.reverseKGroup(head,k)
                break
        return res


a0 = ListNode(0)
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
#a0.next = a1
a1.next = a2
a2.next = a3
a3.next = a4
s = Solution()
tmp = s.reverseKGroup(a0, 1)
while tmp:
    print tmp.val
    tmp = tmp.next
                            