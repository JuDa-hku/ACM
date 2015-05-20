class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        resList,tmpList,tmpLengthWord, tmpWord = [], [],0, 0
        for word in words:
            tmpLengthWord += len(word)
            tmpWord += 1
            if tmpLengthWord+tmpWord-1>maxWidth:
                resList.append(tmpList)
                tmpList,tmpLengthWord, tmpWord = [word], len(word), 1
            else:
                tmpList.append(word)
        resList.append(tmpList)
##we have each line for words
        ans = []
        for i in xrange(len(resList)-1):
            ans.append(self.lineToString(resList[i], maxWidth))
            
        tmpLast = ''
        for word in resList[-1]:
            tmpLast = tmpLast+word+' '
        n = len(tmpLast)
        if n <= maxWidth:
            tmpLast = tmpLast + ' '*(maxWidth-n)
        if n>maxWidth:
            tmpLast = tmpLast[:maxWidth]
        ans.append(tmpLast)
        
        return ans


    def lineToString(self, line, maxWidth):
        numberWords = len(line)
        if numberWords == 1:
            return line[0]+' '*(maxWidth-len(line[0]))
        totalWordLength = 0
        for word in line:
            totalWordLength += len(word)
        lengthLeftForEmpty = maxWidth-totalWordLength
        EmptyBasic = (lengthLeftForEmpty)/(numberWords-1)
        EmptyExtra = (lengthLeftForEmpty)%(numberWords-1)
        res = ''
        for i in xrange(numberWords-1):
            empty = EmptyBasic
            if i<EmptyExtra:
                empty +=  1
            res = res + line[i] + ' '*empty
        res = res + line[numberWords-1]
        return res
        
        
        
        


s= Solution()
words = ["What","must","be","shall","be."]
L = 12
print s.fullJustify(words, L)

                