class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        if n == 0:
            return [0]
        grayCodeNow = [0,1]
        if n == 1:
            return grayCodeNow
        for i in xrange(2,n+1,1):
            tmp = [2**(i-1)+num for num in  grayCodeNow[::-1]]
            grayCodeNow.extend(tmp)
        return grayCodeNow


s = Solution()
print s.grayCode(2)