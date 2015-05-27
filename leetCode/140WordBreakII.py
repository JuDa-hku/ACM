class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        
        n = len(s)
        dp = [[] for i in xrange(n)]
        
        if not self.wordBreakHelp(s, wordDict):
            return []
        
        for i in xrange(n):
#            print i,dp
            for j in xrange(i,-1,-1):
                if s[j:i+1] in wordDict:
                    if j == 0:
                        dp[i].append([s[j:i+1]])
                    elif dp[j-1]:
                        for tmp in dp[j-1]:
                            tmpAdd = tmp[::1]
                            tmpAdd.append(s[j:i+1])
                            dp[i].append(tmpAdd)
        

        res = []
        for tmp in dp[n-1]:
            res.append(' '.join(tmp))
        return res

    def wordBreakHelp(self, s, wordDict):
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
            

sol = Solution()
s = "catsanddog"
wordDict = set(["cat", "cats", "and", "sand", "dog"])
print sol.wordBreak(s, wordDict)
s = "a"
wordDict = set(["a"])
print sol.wordBreak(s, wordDict)
#["cats and dog", "cat sand dog"].

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = set(["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
print sol.wordBreak(s, wordDict)



print sol.wordBreak("aaaaaaa", set(["aaaa","aaa"]))