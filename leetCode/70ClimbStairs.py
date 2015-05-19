class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n <= 1:
            return n
        df = [0 for _ in xrange(n)]
        df[n-1],df[n-2] = 1,2
        for i in xrange(n-3,-1,-1):
            df[i] = df[i+1] + df[i+2]
        return df[0]
        
s = Solution()
for i in xrange(100):
    print s.climbStairs(i)
