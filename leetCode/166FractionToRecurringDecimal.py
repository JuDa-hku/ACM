class Solution:
    # @param numerator, an integer
    # @param denominator, an integer
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if numerator/denominator<0:
            return '-'+self.fractionToDecimal(abs(numerator), abs(denominator))
        intPart = numerator/denominator
        numerator = numerator%denominator
        ## use a list to store the mod
        modList = []
        decimalList = []
        while str(numerator) not in modList:
            if numerator == 0 and len(decimalList) !=0 :
                return str(intPart)+'.'+''.join(decimalList)
            if numerator == 0 and len(decimalList) ==0 :
                return str(intPart)
            modList.append(str(numerator))
            numerator *= 10
            decimalList.append(str(numerator/denominator))
            numerator = numerator%denominator

        ##now the pos of the numerator is the thing we need
        index = [i for i,v in enumerate(modList) if v==str(numerator)]
        index = index[0]
#        decimalList =[str(v) for v in decimalList]
        return str(intPart)+'.'+''.join(decimalList[:index])+'('+''.join(decimalList[index:])+')'
        

s = Solution()
print s.fractionToDecimal(1,3)
print s.fractionToDecimal(2,3)
print s.fractionToDecimal(6,3)
print s.fractionToDecimal(9,4)
print s.fractionToDecimal(-9,4)
print s.fractionToDecimal(0,4)        
            