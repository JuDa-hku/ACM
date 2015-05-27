class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        n = len(ratings)
        if n==0:
            return 0
        res = [1]*n
        for i in xrange(1,n,1):
            if ratings[i]>ratings[i-1]:
                res[i] = res[i-1]+1

        for i in xrange(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                res[i] = max(res[i+1]+1, res[i])
                
        return sum(res)


s = Solution()
print s.candy([1,2,143,45])
