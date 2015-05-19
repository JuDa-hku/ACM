class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in xrange(n)] for _ in xrange(m)]
        dp[m-1][n-1] = grid[m-1][n-1]
        for i in xrange(m-2, -1, -1):
            dp[i][n-1] = grid[i][n-1] + dp[i+1][n-1]
        for i in xrange(n-2, -1, -1):
            dp[m-1][i] = grid[m-1][i] + dp[m-1][i+1]
        for i in xrange(m-2, -1, -1):
            for j in xrange(n-2, -1, -1):
                dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + grid[i][j]
        return dp[0][0]

s = Solution()
grid = [[1]]
print s.minPathSum(grid)
grid = [[1],[2],[3]]
print s.minPathSum(grid)
grid = [[1,2,3],[2,3,4],[3,4,5]]
print s.minPathSum(grid)
