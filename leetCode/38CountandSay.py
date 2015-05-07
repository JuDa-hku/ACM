class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        res = "1"
        for _ in xrange(n-1):
            res = self.generateNext(res)
        return res

    def generateNext(self, string):
        string = string +'#'
        count,i,res = 1,0,""
        while i != len(string)-1:
            if string[i] == string[i+1]:
                count += 1
                i += 1
            else:
                res = res+str(count) + string[i]
                i += 1
                count = 1
        return res

s = Solution()
#print s.generateNext("21")
print s.countAndSay(6)
            
            