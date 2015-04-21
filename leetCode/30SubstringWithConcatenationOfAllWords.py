class Solution:
    # @param S, a string
    # @param L, a string[]
    # @return an integer[]
    def checkDict(self, wordDict):
        for key, value in wordDict.iteritems():
            if value != 0:
                return False
        return True

    def makeDict(self, L, wordDict):
        for word in L:
            if word in wordDict:
                wordDict[word] += 1
            else:
                wordDict[word] = 1

    def initDict(self, wordDict, S, wordLength):
        newWordDict = {k:v for k,v in wordDict.iteritems()}
        for i in xrange(0, len(S), wordLength):
            word = S[i:i+wordLength]
            if word in wordDict:
                newWordDict[word] -= 1
        return newWordDict
    
        
    def findSubstring(self, S, L):
        result, wordDict = [], {}
        wordLength = len(L[0])
        totalLength = wordLength*len(L)
        circleTime = len(S)/wordLength + 1
        self.makeDict(L, wordDict)
        for start in xrange(wordLength):
            for i in xrange(circleTime):
                realStart = start + i*wordLength
                if realStart+totalLength-1 > len(S)-1:
                    break
                if i == 0:
                    newWordDict = self.initDict(wordDict, S[realStart:realStart+totalLength], wordLength)
 #                   print newWordDict, wordDict, S[realStart:realStart+totalLength]
                else:
                    wordRemove = S[realStart-wordLength:realStart]
                    wordAdded = S[realStart+totalLength-wordLength: realStart+totalLength]
                    if wordRemove in newWordDict:
                        newWordDict[wordRemove] += 1
                    if wordAdded in newWordDict:
                        newWordDict[wordAdded] -= 1
#                    print newWordDict, wordRemove, wordAdded
                if self.checkDict(newWordDict):
                    result.append(realStart)
        return result

s = Solution()
S = 'ababaab'
L = ["ab", "ba", "ba"]
S1 = "foobar"
print s.findSubstring(S, L)
# print s.findSubstring(S1, L)
# S = "abababba"
# L = ["ab","ba","ab"]
# print s.findSubstring(S, L)
# #the length for each word is the same.


# S = "ab"*10000
# L =['ab','ba']
# print s.findSubstring(S, L)



# class Solution:
#     # @param S, a string
#     # @param L, a list of string
#     # @return a list of integer
#     def findSubstring(self, S, L):
#         if not L or not L[0]: return None
#         wl = len(L[0])
#         totl = len(L) * wl
#         count_tmpl = collections.defaultdict(int)
#         for word in L: count_tmpl[word] += 1
#         rtn = []
#         for i in range(wl):
#             count = copy.copy(count_tmpl)
#             j = i
#             while j < len(S)-wl+1:
#                 count[S[j:j+wl]] -= 1
#                 while count[S[j:j+wl]] < 0:
#                     count[S[i:i+wl]] += 1
#                     i += wl
#                 j += wl
#                 if j-i == totl: rtn.append(i)
#         return rtn
