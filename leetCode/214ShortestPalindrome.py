class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        n = len(s)
        leftLength = n/2
        while leftLength >=0:
            if s[:leftLength] == s[leftLength+1:leftLength*2+1]:
                return s[n:leftLength*2:-1] + s
            if s[:leftLength] == s[leftLength:leftLength*2]:
                return s[n:leftLength*2-1:-1] + s
            leftLength -= 1

    def shortestPalindrome(self, s):
        r=s[::-1];

        left=s[1:][::-1];
        middle= len(s)//2+1;
        while(middle>=0):
            if(r[len(s)-middle:]==s[middle+1:middle+1+middle]):
                left=s[middle+1+middle:][::-1];
                break;
            if(r[len(s)-middle:]==s[middle:middle+middle]):
                left=s[middle+middle:][::-1];
                break;
            middle-=1;

        return left+s;


        
##kmp algorithm
class Solution:
# @param {string} s
# @return {string}
    def shortestPalindrome(self, s):
        A=s+s[::-1]
        cont=[0]
        for i in range(1,len(A)):
            index=cont[i-1]
            while(index>0 and A[index]!=A[i]):
                index=cont[index-1]
            cont.append(index+(1 if A[index]==A[i] else 0))
        return s[cont[-1]:][::-1]+s

        



        

        
s = Solution()
print s.shortestPalindrome("abcd")

            
        

            