class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        listA = [i for i in a]
        listB = [i for i in b]
        if len(listA)>len(listB):
            return self.addBinary(b, a)
        res,carry = [], 0
        listA, listB = listA[::-1], listB[::-1]
        for i in xrange(len(listA)):
            tmp = int(listA[i])+int(listB[i])+carry
            carry = tmp/2
            left = tmp%2
            res.append(str(left))
        if len(listA) == len(listB):
            if carry == 1:
                res.append(str(carry))
            return ''.join(res[::-1])
        for i in xrange(len(listA),len(listB),1):
            tmp = carry + int(listB[i])
            carry = tmp/2
            left = tmp%2
            res.append(str(left))
        if carry == 1:
            res.append(str(carry))
        return ''.join(res[::-1])
        
s = Solution()
a = '11'
b = '11'
print s.addBinary(a,b)