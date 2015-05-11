class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        dp = [[1 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(2, m+1,1):
            for j in range(2, n+1,1):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

s = Solution()
print s.uniquePaths(2,2)