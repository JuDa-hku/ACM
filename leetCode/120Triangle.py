class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        n = len(triangle)
        if n == 0:
            return 0
        if n == 1:
            return min(triangle[0])
        dp = triangle[n-1][::1]
        
        for i in xrange(n-2, -1, -1):
            for j in xrange(len(dp)-1):
                dp[j] = min(triangle[i][j]+dp[j+1], triangle[i][j]+dp[j])
            dp.pop()

        return dp[0]

s = Solution()
print s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])

