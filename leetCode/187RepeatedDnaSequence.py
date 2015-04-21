class Solution:
    # @param s, a string
    # @return a string[]
    def findRepeatedDnaSequences(self, s):
        result = []
        dic = {}
        Length = len(s)
        if Length<=10:
            return result
        for start in xrange(len(s)-9):
            key = s[start:start+10]
            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1
        result = [key for key,value in dic.items() if value>1]
        return result


s = 'A'*11
a = Solution()
s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
s = "GAGAGAGAGAGAG"
print a.findRepeatedDnaSequences(s)
            