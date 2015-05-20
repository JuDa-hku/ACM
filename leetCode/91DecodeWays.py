class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        n = len(s)
        if n==0:
            return 0
        if s[0] == '0':
            return 0
        if n == 1:
            return 1
        dp = [1]*n
        if int(s[0:2])<=26 and s[1]!='0':
            dp[1] = 2
        if int(s[0:2])>26 and s[1]=='0':
            return 0
        
        for i in xrange(2,n,1):
            if s[i] == '0' and s[i-1] !='1' and s[i-1] !='2':
                return 0
            elif int(s[i-1:i+1:1])<=26 and s[i]!='0' and s[i-1]!='0':
                dp[i] = dp[i-1]+dp[i-2]
            elif int(s[i-1:i+1:1])<=26 and s[i]=='0':
                dp[i] = dp[i-2]
            elif int(s[i-1:i+1:1])<=26 and s[i-1]=='0':
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[n-1]

s = Solution()
print s.numDecodings('101')

            
        