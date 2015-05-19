class Solution:
    def romanToInt(self, s):
        romDict = {1000:'M', 2000:'MM', 3000:'MMM',100:'C', 200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM', 10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC',1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
        newDict = {}
        for key in romDict:
            newDict[romDict[key]] = key
#        print newDict
        
        res = newDict[s[-1]]
        for i in range(len(s)-2, -1, -1):
            tmp, tmp1 = newDict[s[i]], newDict[s[i+1]]
            if tmp>=tmp1:
                res += tmp
            else:
                res -= tmp
        return res
            


s = Solution()
print s.romanToInt('MMMCM')

            