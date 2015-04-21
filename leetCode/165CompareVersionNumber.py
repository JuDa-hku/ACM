class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        str1 = version1.split('.')
        str2 = version2.split('.')
        if len(str1)<len(str2):
            str1.extend([0]*(len(str2)-len(str1)))
        if len(str2)<len(str1):
            str2.extend([0]*(len(str1)-len(str2)))
        for num1, num2 in zip(str1, str2):
            num1,num2 = float(num1), float(num2)
            if num1<num2:
                return -1
            if num1>num2:
                return 1
        else:
            return 0

s = Solution()            
print s.compareVersion('01', '1.1')