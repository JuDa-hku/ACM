class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        if len(s) == 0:
            return 0
        dpPvalue, dpLength = [0 for _ in s], [0 for _ in s]
        if s[0] == '(':
            dpPvalue[0] = 1
        if s[0] == ')':
            dpPvalue[0] = -1
        for i in xrange(1,len(s),1):
            if s[i] == '(':
                dpPvalue[i] = max(dpPvalue[i-1],0) + 1
                dpLength[i] = 0
            if s[i] == ')':
                dpPvalue[i] = max(dpPvalue[i-1],0)-1
                if dpPvalue[i]>=0:
                    dpLength[i] = dpLength[i-1] + 2
#                    print i, dpLength[i]
                    if s[i-dpLength[i]] == ')' and i-dpLength[i]>0:
                        dpLength[i] += dpLength[i-dpLength[i]]
#        print dpLength, dpPvalue
        return max(dpLength)

s = Solution()
string ="((()))))(((())))"
print s.longestValidParentheses(string)
string = ")()())"
print s.longestValidParentheses(string)
string = "()()"
print s.longestValidParentheses(string)
string = ")))"
print s.longestValidParentheses(string)
string = "()(()"
print s.longestValidParentheses(string)
string = "(()()"
print s.longestValidParentheses(string)
string ="()"
print s.longestValidParentheses(string)


# another clear way
def longestValidParentheses_dp2(self,s):
    l=len(s)
    DP=[i for i in range(l)]
    result=0
    stack=[]
    for i in range(l):
        if s[i]=='(':
           stack.append(i) 
        else:
            if stack:
                last=stack.pop()
                DP[i]=last
                ## find the one to one ()
                if last>1 and DP[last-1]!=last-1:
                ##if the previous is ) and has the ( to it. let the i to the earliest (
                    DP[i]=DP[last-1]
        if DP[i]!=i:
            ##find the "()" calculate the length for case ()()
            result=max(result,i-DP[i]+1)
    return result


