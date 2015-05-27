# Definition for singly-linked list with a random pointer.
class RandomListNode:
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        seen = {}
        if not head:
            return None
        return self.copyRandomListHelp(head, seen)
        

    def copyRandomListHelp(self, head, seen):
        if not head:
            return None
        if head in seen:
            newHead = seen[head]
        else:
            newHead = RandomListNode(head.label)
        if head.random:
            if head.random in seen:
                newHead.random = seen[head.random]
            else:
                randomNode = RandomListNode(head.random.label)
                seen[head.random] = randomNode
                newHead.random = randomNode
        nextHead = self.copyRandomListHelp(head.next, seen)
        newHead.next = nextHead
        return newHead


a0, a1, a2 = RandomListNode(0),RandomListNode(1),RandomListNode(2)
a0.next, a1.next = a1, a2
a0.random = a2
a1.random = a0
a2.random = a0
s = Solution()
b0 = s.copyRandomList(a0)
