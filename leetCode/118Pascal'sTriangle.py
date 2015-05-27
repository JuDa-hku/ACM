class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1,numRows,1):
            tmp = [1]*(i+1)
            for j in xrange(i+1):
                if  0<j<i:
                    tmp[j] = res[i-1][j-1] + res[i-1][j]
            res.append(tmp)
        return res

s = Solution()
print s.generate(5)