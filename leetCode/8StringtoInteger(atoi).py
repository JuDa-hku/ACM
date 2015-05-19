class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, xString):
        xString = xString.strip(' ')
        xList = [i for i in xString]
        newList = []
        if len(xList) == 0:
            return 0

        i = 0
        while i<len(xList):
            if xList[i] == '-':
                tag = True
                i += 1
                break
            elif xList[i] == '+':
                i += 1
                tag = False
                break
            elif '0'<=xList[i]<='9':
                newList.append(xList[i])
                tag = False
                i += 1
                break
            else:
                return 0
        
            
        for s in xList[i:]:
            if '0'<=s<='9':
                newList.append(s)
            else:
                break
                
        if len(newList) == 0:
            return 0

        while True:
            if newList[0] != '0' or len(newList) == 1:
                break
            if newList[0] == '0':
                newList.pop(0)
            
        reverseXString = ''.join(newList)
        if tag and int(reverseXString)>2**31:
            return -2**31
        if not tag and int(reverseXString)>2**31-1:
            return 2**31-1
        if tag:
            return -int(reverseXString)
        if not tag:
            return int(reverseXString)



s = Solution()
print s.myAtoi('  ')
print s.myAtoi(' 10 ')
print s.myAtoi(' +-2 ')
print s.myAtoi(' -e010ef ')
print s.myAtoi(' 01000000000003 ')