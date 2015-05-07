import collections
class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}

    def isScramble(self, s1, s2):
        if len(s1)!=len(s2) or sorted(s1) != sorted(s2):
            return False
        if len(s1)<4:
            return True
        n = len(s1)
        for i in xrange(1, n, 1):
            tmp1 = self.isScramble(s1[:i], s2[:i])
            tmp2 = self.isScramble(s1[i:], s2[i:])
            tmp3 = self.isScramble(s1[:i], s2[n-i:])
            tmp4 = self.isScramble(s1[i:], s2[:n-i])
#            print tmp3,tmp4, s1[:i],s1
            if (tmp1 and tmp2) or (tmp3 and tmp4):
                return True
        return False
    

s1 = "ggreat"
s2 = "rgeat"
s3 = "rgtae"
s4 = "rggtae"
s = Solution()
print s.isScramble(s1,s2)
print s.isScramble(s1,s4)
s1,s4 = 'abcd','dacb'
print s.isScramble(s1,s4)
s1 = "pcighfdjnbwfkohtklrecxnooxyipj"
s4 = "npodkfchrfpxliocgtnykhxwjbojie"
print s.isScramble(s1,s4)