class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.strip(" ")
        l = s.split(' ')
        l = l[::-1]
        newl = [ch for ch in l if ch!='']
        return ' '.join(newl)

s = Solution()
print s.reverseWords("the sky is    blue ")