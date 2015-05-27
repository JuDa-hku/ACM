class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        if len(s) == 0:
            return 0
        tmp, tmp1 = 0, 0
        for i in xrange(len(s)):
            if s[i] == t[0]:
                tmp = i
                break

        for i in xrange(len(s)-1, -1, -1):
            if s[i] == t[-1]:
                tmp1 = i
                break
        
        s = s[tmp:tmp1+1]

        news = ''
        for i in xrange(len(s)):
            if s[i]  in t:
                news += s[i]
#        print news
        s = news
                
        m, n = len(s), len(t)
        if n>m:
            return 0
        if n == m:
            if s == t:
                return 1
            else:
                return 0
        dp = [[0]*m for _ in xrange(n)]
        if s[0] == t[0]:
            dp[0][0] = 1
        for j in xrange(1,m,1):
            if s[j] == t[0]:
                dp[0][j] = dp[0][j-1] + 1
            else:
                dp[0][j] = dp[0][j-1]
                
        for i in xrange(1,n,1):
            for j in xrange(i,m,1):
                if t[i] != s[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
#        print dp
        return dp[n-1][m-1]
        
                    
s = Solution()
S = "rabbbit"
T = "rabbit"
print s.numDistinct("abacadaefghi", "a")