class Solution:
    # @param n, an integer
    # @return an integer
    def toBinary(self, n):
        return ''.join(str(1&n>>i) for i in range(32)[::-1])
    def toInt(self, binN):
        result = 0
        for  index,bin in enumerate(binN[::-1]):
            result += int(bin)*(2**index)
        return result
    
    def reverseBits(self, n):
        binN = self.toBinary(n)
        binN = binN[::-1]
        return self.toInt(binN)
        
        
a = Solution()        
print a.reverseBits(43261596)