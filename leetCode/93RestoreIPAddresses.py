class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        count, res, resList = 0, '', []
        self.restoreIpAddressesHelp(s, count, res, resList)
        return resList


    def restoreIpAddressesHelp(self, s, count, res, resList):
        if len(s)>3*(4-count):
            return
        elif len(s) == 0 and count == 4:
            newRes = res[:len(res)-1]
            resList.append(newRes)
            return
        elif len(s) == 0 and count != 4:
            return
        elif s[0] == '0':
            tmpS = s[1:]
            tmpRes = res+'0'+'.'
            self.restoreIpAddressesHelp(tmpS, count+1, tmpRes, resList)
        else:
            maxLengthPer = min(3, len(s))
            for i in range(0,maxLengthPer,1):
                if int(s[:i+1])<=255:
                    tmpS = s[i+1:]
                    tmpRes = res+s[:i+1]+'.'
                    print tmpS, tmpRes
                    self.restoreIpAddressesHelp(tmpS, count+1, tmpRes, resList)
                else:
                    return
        
                
s = Solution()
print s.restoreIpAddresses("0000")