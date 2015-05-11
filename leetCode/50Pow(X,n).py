class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n<0:
            return self.myPow(1./x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        if n%2 == 0:
            tmp = self.myPow(x, n/2)
            return tmp**2
        if n%2 == 1:
            return self.myPow(x, n-1)*x

s = Solution()
print s.myPow(2, 0)
print s.myPow(2, -10)