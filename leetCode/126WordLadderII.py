from collections import deque, defaultdict
class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def findLadders(self, beginWord, endWord, wordDict):
        candidateDict = wordDict
        candidateDict.add(endWord)
        candidateDict.add(beginWord)
        res = defaultdict(set)
        parentSet = set()
        parentSet.add(beginWord)
        endTag = False
        
        while parentSet:
            tmpSet = set()
            candidateDict.difference_update(parentSet)
            for tmp in parentSet:
                for i in range(len(tmp)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nextWord = tmp[:i] + c + tmp[i+1:]
                        if nextWord == endWord:
                            res[nextWord].add(tmp)
                            endTag = True
                        elif nextWord in candidateDict:
#                            print tmp, nextWord
                            res[nextWord].add(tmp)
                            tmpSet.add(nextWord)
            if endTag:
                break
            parentSet = tmpSet
        listRes = self.generateList(res, beginWord, endWord)
        return listRes
        
    def generateList(self, res, beginWord, endWord):
        listRes = []
        if beginWord == endWord:
            return [[endWord]]
        for word in res[endWord]:
            listRes += self.generateList(res, beginWord, word)
        for path in listRes:
            path.append(endWord)
        return listRes



        
    




s = Solution()
start, end = 'a', 'c'
wordDict = set(["a","c"])
print s.findLadders(start, end, wordDict)
print s.findLadders("red", "tax", set(["ted","tex","red","tax","tad","den","rex","pee"]))

