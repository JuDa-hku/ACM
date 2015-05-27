class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        res, nextRes = [1], [1]
        for i in range(1,rowIndex+1,1):
            for j in xrange(i+1):
                if  0<j<i:
                    nextRes[j] = res[j-1] + res[j]
            nextRes.append(1)
            res = nextRes[::1]
        return res

s = Solution()
print s.getRow(0)