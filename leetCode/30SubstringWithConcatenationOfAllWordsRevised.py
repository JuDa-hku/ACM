import copy
from collections import defaultdict
class Solution:
    # @param S, a string
    # @param L, a string[]
    # @return an integer[]
    def findSubstring(self, S, L):
        wordLength = len(L[0])
        totalLength = len(L)*wordLength
        wordDict = defaultdict(int)
        res = []
        for word in L:
            wordDict[word] += 1
        for i in range(wordLength):
            tmpDict = copy.copy(wordDict)
            j = i
            while j<len(S)-wordLength+1:
                wordConsidered = S[j:j+wordLength]
                tmpDict[wordConsidered] -= 1
                if tmpDict[wordConsidered] < 0:
                    while tmpDict[wordConsidered] < 0:
                        tmpDict[S[i:i+wordLength]] += 1
                        i = i+wordLength
                j = j+wordLength
                if j-i == totalLength:
                    res.append(i)
                

        return res


s = Solution()
S = 'baabbaba'
L = ["ab", "ba", "ba"]
S1 = "foobar"
print s.findSubstring(S, L)