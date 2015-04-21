class Solution:
    # @param num, an integer[]
    # @return a string
    

    def cmpfunc(self,num1, num2):
        str1, str2 = str(num1), str(num2)
        # if len(str1) == len(str2):
        #     for a,b in zip(str1, str2):
        #         if a<b:
        #             return -1
        #         if a>b:
        #             return 1
        #     return 0
        if len(str1)>len(str2):
            return -self.cmpfunc(num2, num1)
        str3 = str1+str1[0]*(len(str2)-len(str1))
        for a,b in zip(str3, str2):
            if a<b:
                return -1
            if a>b:
                return 1
        for char in str1:
            if char<str1[0]:
                return -1
            if char>str1[0]:
                return 1
        return 0
                
        
    def largestNumber(self, num):
        num = sorted(num, cmp=self.cmpfunc)
        num = num[::-1]
        strNum = [str(n) for n in num]
        if len(strNum)>1 and strNum[0]=='0':
            return "0"
        return ''.join(strNum)

s = Solution()
num = [1,2,21,34,9,98]
num = [3,30,34,5,9]
num = [12,121]
num = [0,0]
print s.largestNumber(num)
