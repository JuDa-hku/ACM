# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        faster, slower = head, head
        while  faster and  faster.next and  slower:
            faster = faster.next.next
            slower = slower.next
            if faster == slower:
                return True
        return False


        
a1,a2 = ListNode(1), ListNode(2)
a1.next, a2.next = a2, a1
s = Solution()
print s.hasCycle(a1)