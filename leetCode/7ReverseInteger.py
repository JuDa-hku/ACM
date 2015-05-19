class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        xString = str(x)
        xList = [i for i in xString]
        if xList[0] == '-':
            tag = True
            newxList=xList[:0:-1]
        else:
            tag = False
            newxList = xList[::-1]
        while True:
            if newxList[0] != '0' or len(newxList) == 1:
                break
            if newxList[0] == '0':
                newxList.pop(0)
        reverseXString = ''.join(newxList)
        if tag and int(reverseXString)>2**31:
            return -1
        if not tag and int(reverseXString)>2**31-1:
            return -1
        if tag:
            return -int(reverseXString)
        if not tag:
            return int(reverseXString)

s = Solution()
print s.reverse(-10)