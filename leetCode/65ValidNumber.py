class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        s = s.strip(' ')
        if len(s) ==0:
            return False
        if not self.regularCheck(s):
            return False
        if 'e' in s:
            return self.checkScience(s)
        if '.' in s:
            return self.checkDigit(s)
        else:
            return self.checkNumber(s)

    def regularCheck(self, s):
        for a in s:
            if a=='.' or a=='e' or a=='-' or a=='+':
                continue
            if '0'<=a<='9':
                continue
            else:
                return False
        return True

    def checkNumber(self, s):
        if len(s) == 0:
            return False
        if len(s) == 1 and '0'<=s[0]<='9':
            return True
        tmp = s
        if s[0] == '-' or s[0] == '+':
            tmp = s[1:]
        if len(tmp) == 0:
            return False
        for a in tmp:
            if not '0'<=a<='9':
                return False
        return True
        
    def checkDigit(self, s):
        if len(s) == 1:
            return False
        if s[0] == '-' or s[0]=='+':
            s = s[1:]
        if len(s) == 1:
            return False
        if len(s)<2:
            return True
        # if s[0] == '.' or s[-1]=='.':
        #     return False
        if s[-1]==0 and s[-2]==0:
            return False
        if s[0]==0 and s[1]==0:
            return False
        noneZeroFlag,digitFlag = False, False
        for a in s:
            if a == '.' and not digitFlag:
                digitFlag = True
            elif a =='.' and digitFlag:
                return False
            elif '0'<a<='9':
                noneZeroFlag = True
            elif a == '0':
                continue
            else:
                return False
        return True
        
    
    def checkScience(self, s):
        if len(s) == 0:
            return False
        if len(s)<2:
            return False
        for i in xrange(len(s)):
            if s[i] == 'e':
                break
        if i==len(s)-1:
            return False
        if '.' in s[:i]:
            tmp1 = self.checkDigit(s[:i])
        if '.' not in s[:i]:
            tmp1 = self.checkNumber(s[:i])
        tmp2 = self.checkNumber(s[i+1:])
        return tmp1 and tmp2



s = Solution()
print s.checkDigit('0.01')
print s.checkDigit('0.1')
print s.checkDigit('.1')
print s.checkDigit('1.0')
print s.checkScience('1e1')
print s.checkScience('1e10')
print s.checkScience('1.e10')
print s.isNumber(' 1ea00 ')
print s.isNumber(' e9 ')
print s.isNumber('.8 ')
print s.isNumber('51.80 ')

        
        