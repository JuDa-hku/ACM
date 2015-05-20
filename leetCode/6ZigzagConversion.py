class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        stringList = ['' for _ in xrange(numRows)]
        if numRows == 1:
            return s
        for index in xrange(len(s)):
            ncol = index%(2*numRows-2)
            if ncol<numRows:
                ncol = ncol
            elif ncol>=numRows:
                ncol = numRows - ncol%(numRows)-2
            stringList[ncol] += s[index]
        res = ''
        for string in stringList:
            res += string
        return res


s = Solution()
string = "PAHNAPLSIIGYIR"
string = "PAYPALISHIRING"
print s.convert(string, 2)
            