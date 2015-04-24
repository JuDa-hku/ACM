class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesisBack(self, initStr, leftPSize, rightPsize,maxSize, Res):
        if leftPSize == maxSize and rightPsize==maxSize and self.isValid(initStr):
            Res.add(initStr)
        elif leftPSize>maxSize  or rightPsize>maxSize or not self.isValid(initStr): 
            return
        else:
            for s in ['(', ')']:
                self.generateParenthesisBack(initStr+s, leftPSize+int(s=='('), rightPsize+int(s==')'), maxSize, Res)


                
    def isValid(self, initStr):
        stack = []
        for s in initStr:
            if s == '(':
                stack.append(s)
            if s == ')':
                if not stack:
                    return False
                else:
                    stack.pop(0)
        return True
        
        
        
    def generateParenthesis(self, n):
        Res, initStr = set(), ''
        self.generateParenthesisBack(initStr, 0, 0, n, Res)
        return Res

s = Solution()
print  s.generateParenthesis(3)