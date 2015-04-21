class Solution:
    # @param s, a string
    # @return a boolean
    def isValid(self, s):
        stackParentheses = []
        leftParenthese, rightParenthese = ['(','[','{'], [')',']','}']
        parenthestDict = {'(':')', '[':']', '{':'}'}
        for i in s:
            if i in leftParenthese:
                stackParentheses.append(i)
            if i in rightParenthese and len(stackParentheses) == 0:
                return False
            if i in rightParenthese and len(stackParentheses) != 0:
                check = stackParentheses.pop()
                if parenthestDict[check] != i:
                    return False
        if len(stackParentheses) == 0:
            return True
        else:
            return False

s = Solution()
x1 = '[()]'
x2 = '[[()]'
print s.isValid(x1)
print s.isValid(x2)
                