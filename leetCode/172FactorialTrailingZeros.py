class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        #count num of 5
        m = n
        while m>=5:
             countFive =  m/5+countFive
             m = m/5
        return countFive

s = Solution()
print s.trailingZeroes(11)
print s.trailingZeroes(5)
print s.trailingZeroes(10)