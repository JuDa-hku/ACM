class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        indexUnique = 0
        if len(A)<=1:
            return len(A)
        for i in xrange(len(A)):
            if (A[i] != A[indexUnique]):
                indexUnique += 1
                A[indexUnique] = A[i]
        for i in range(indexUnique+1, len(A)):
            A.pop()
        return indexUnique+1


a = [1,1,2,2]
s = Solution()
print s.removeDuplicates(a)

