class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
#        print s1, s2, s3
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        if s1[0] != s3[0] and s2[0]!=s3[0]:
            return False
        if s1[0] == s3[0] and s2[0] == s3[0]:
            if len(s1) == 1:
                return self.isInterleave(s1, s2[1:], s3[1:])
            if len(s2) == 1:
                return self.isInterleave(s1[1:], s2, s3[1:])
            if s1[1] == s1[0] and s3[1] == s3[0] and s2[1] != s2[0]:
                return self.isInterleave(s1[1:], s2, s3[1:])
            if s1[1] == s1[0] and s3[1] != s3[0] and s2[1] != s2[0]:
                return self.isInterleave(s1, s2[1:], s3[1:])
            if s2[1] == s2[0] and s3[1] == s3[0] and s1[1] != s1[0]:
                return self.isInterleave(s1, s2[1:], s3[1:])
            if s2[1] == s2[0] and s3[1] != s3[0] and s1[1] != s1[0]:
                return self.isInterleave(s1[1:], s2, s3[1:])
            else:
                return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
        if s1[0] == s3[0] and s2[0] != s3[0]:
            return self.isInterleave(s1[1:], s2, s3[1:])
        if s2[0] == s3[0] and s1[0] != s3[0]:
            return self.isInterleave(s1, s2[1:], s3[1:])


##transform the recrusive code to the dynamic code
class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        if len(s1)+len(s2) != len(s3):
            return False
        dp = [[False for _ in xrange(len(s2)+1)] for _ in xrange(len(s1)+1)]
        dp[0][0] = True
        for j in xrange(1, len(s2)+1, 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in xrange(1, len(s1)+1, 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for i in xrange(1, len(s1)+1,1):
            for j in xrange(1, len(s2)+1,1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
 #       print dp
        return dp[-1][-1]
            
        
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s4 = "aadbbbaccc"        
s = Solution()
print s.isInterleave(s1,s2,s3)
print s.isInterleave(s1,s2,s4)
print s.isInterleave("aa", "ab", "aaba")
print s.isInterleave("aabc", "abad", "aabcabad")
print s.isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab")
