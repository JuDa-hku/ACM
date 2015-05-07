class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        n1, n2, cache = len(num1), len(num2), {}
        if n2>n1:
            return self.multiply(num2, num1)
        res = "0"
        num3 = num2[::-1]
        for i in xrange(n2):
            numberZero, tmp = "0"*i, "0"
            if num3[i] in cache:
                tmp = cache[num3[i]]
            else:
                for j in xrange(int(num3[i])):
                    tmp = self.add(num1, tmp)
                cache[num3[i]] = tmp
            tmpPosI= tmp + numberZero
            res = self.add(tmpPosI, res)
        return res
        
        
    def add(self, num1, num2):
        if len(num1)<len(num2):
            return self.add(num2, num1)
        if len(num2) == 0:
            return num1
        n1, n2 = len(num1), len(num2)
        lastAdd = int(num1[-1])+int(num2[-1])
        if lastAdd < 10:
            return self.add(num1[:(n1-1)], num2[:(n2-1)]) + str(lastAdd)
        if lastAdd >= 10:
            tmp = self.add(num1[:(n1-1)], "1")
            return  self.add(tmp, num2[:(n2-1)]) + str(lastAdd%10)

s= Solution()
print s.multiply("379793381910974090173405088322972943", "4515503214242784384118516920342794464987611881430043826418762953520018971372435632")

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        n1, n2 = len(num1), len(num2)
        sumStr = ['0']*(n1+n2)
        num3, num4 = num1[::-1], num2[::-1]
        for i in xrange(n1):
            carry = 0
            for j in xrange(n2):
                tmp = int(num3[i])*int(num4[j]) + int(sumStr[i+j]) + carry
                sumStr[i+j] = str(tmp%10)
                carry = tmp/10
#                print i,j, tmp,sumStr, carry
            sumStr[i+n2] = str(carry + int(sumStr[i+n2]))
        while True:
            if len(sumStr) == 0:
                return "0"
            if sumStr[-1] == "0":
                sumStr.pop()
            else:
                break
        return "".join(sumStr[::-1])
            
s = Solution()
print s.multiply("773", "10")
print s.multiply("379793381910974090173405088322972943", "4515503214242784384118516920342794464987611881430043826418762953520018971372435632")
# print s.multiply("3910859239577049200280", "44409373865962")
# print s.multiply("971760341161", "8455738366101455974611535948671636301137077335932515768462241304266372179032527079565403847080606555763")
# print s.multiply("63068080726329880611684115603801120940144776974937025638198670884099005492080675397052881650850279", "0")
