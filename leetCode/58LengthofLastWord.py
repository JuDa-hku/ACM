class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        stringList = s.split(' ')
#        print stringList
        lengthOfEachWord = [len(i) for i in stringList]
        while lengthOfEachWord:
            if lengthOfEachWord[-1] == 0:
                lengthOfEachWord.pop()
            else:
                return lengthOfEachWord[-1]
        return 0


s = Solution()
print s.lengthOfLastWord("hello World")
print s.lengthOfLastWord("")
print s.lengthOfLastWord("a ")