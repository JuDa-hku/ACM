class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False]*n
        for i in xrange(n):
            for j in xrange(i,-1,-1):
                if dp[i]:
                    break
                if s[j:i+1] in wordDict:
                    if j == 0:
                        dp[i] = True
                    else:
                        dp[i] = dp[i] or dp[j-1]
        return dp[n-1]
            
        
        


s = Solution()
print s.wordBreak("a", set(["a"]))
print s.wordBreak("leetcode", set(["leet","code"]))
print s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", set(["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
