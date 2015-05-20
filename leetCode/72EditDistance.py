class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        n1, n2 = len(word1), len(word2)
        dp = [[0]*(n2+1) for _ in xrange(n1+1)]
        for i in xrange(n1+1):
            for j in xrange(n2+1):
                if i==0 or j==0:
                    dp[i][j] = max(i,j)
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif word1[i-1] != word2[j-1]:
                    tmp1 = dp[i-1][j] + 1
                    tmp2 = dp[i][j-1] + 1
                    tmp3 = dp[i-1][j-1] + 1
                    dp[i][j] = min(tmp1, tmp2, tmp3)

        return dp[-1][-1]



class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        n1, n2 = len(word1), len(word2)
        curr, pre = [0]*(n2+1), [0]*(n2+1)
        for i in xrange(n1+1):
            pre = [c  for c in curr]
            for j in xrange(n2+1):
                if i==0 or j==0:
                    curr[j] = max(i,j)
                elif word1[i-1] == word2[j-1]:
                    curr[j] = pre[j-1]
                elif word1[i-1] != word2[j-1]:
                    tmp1 = pre[j] + 1
                    tmp2 = curr[j-1] + 1
                    tmp3 = pre[j-1] + 1
                    curr[j] = min(tmp1, tmp2, tmp3)
        return curr[-1]

s = Solution()
word1 = 'abcd'
word2 = 'e'
print s.minDistance(word1, word2)

            
        
        