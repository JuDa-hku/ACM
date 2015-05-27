from collections import deque
class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        candidateDict = wordDict
        stack = deque([(beginWord,1)])

        
        while stack:
            checkedSet = set()
            tmp = stack.popleft()
            for i in range(len(tmp[0])):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = tmp[0][:i] + c + tmp[0][i+1:]
                    if nextWord == endWord:
                        return tmp[1]+1
                    elif nextWord in candidateDict and nextWord!=beginWord:
                        checkedSet.add(nextWord)
                        stack.append((nextWord, tmp[1]+1))
            candidateDict.difference_update(checkedSet)
        return 0




s = Solution()
start, end = 'hit', 'cog'
wordDict = set(["hot","dot","dog","lot","log"])
print s.ladderLength(start, end, wordDict)

start, end = "qa", "sq"
wordDict = set(["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"])
print s.ladderLength(start, end, wordDict)