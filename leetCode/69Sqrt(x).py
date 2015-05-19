class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        res = self.mySqrtHelp(x, 0, x+1)
        return res
        
    def mySqrtHelp(self, x, lower, higher):
        middle = (lower+higher)/2
        if middle*middle<=x and (middle+1)*(middle+1)>x:
            return middle
        if middle*middle>x:
            return self.mySqrtHelp(x, lower, middle)
        if middle*middle<=x and (middle+1)*(middle+1)<=x:
            return self.mySqrtHelp(x,middle, higher)
        
s = Solution()
print s.mySqrt(102194914001491410494)