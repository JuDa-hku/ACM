class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if len(p) ==0 and len(s)!=0:
            return False
        dp = [[False]*(len(p) + 1) for _ in range(len(s)+1)]
        dp[0][0] = True
        for i in range(1, len(s)+1, 1):
            dp[i][0] = False
        for j in range(1, len(p), 1):
            dp[0][j+1] = dp[0][j-1] and p[j] == '*'
        for i in range(1, len(s)+1, 1):
            for j in range(1, len(p)+1, 1):
                if p[j-1] != "*" and p[j-1] != ".":
                    dp[i][j] = (dp[i-1][j-1] and s[i-1] == p[j-1])
                if p[j-1] == "*" and p[j-2] == ".":
                    dp[i][j] = False
                    if j-2 == 0:
                        dp[i][j] = True
                    else:
                        for tmp in xrange(i+1):
                            if dp[tmp][j-2]:
                                dp[i][j] = True
                if p[j-1] == "*" and p[j-2]!= ".":
                    dp[i][j] = (dp[i-1][j-1] and s[i-1] == p[j-2]) or dp[i][j-2] or dp[i][j-1]
                if p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
        #print dp
        return dp[-1][-1]
        
s = Solution()
print s.isMatch("aa", "a")
print s.isMatch("aa", "aa")
print s.isMatch("aaa", "a")
print s.isMatch("aa", "a*")
print s.isMatch("aa", ".*")
print s.isMatch("aab", "c*a*b")
print s.isMatch("abcd", ".bcd")
print s.isMatch("aa", "aab*")
