import math
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n<=2:
            return 0
        passed = [True]*n

        
        for i in xrange(3, int(math.sqrt(n))+1, 2):
            if passed[i]:
                k = i<<1
                for j in xrange(i*i, n, k):
                    if j < n:
                        passed[j] = False

        res = 1
        for i in xrange(3, n, 2):
            if passed[i]:
                res += 1
        return res
        

s = Solution()
print s.countPrimes(4)
            
        