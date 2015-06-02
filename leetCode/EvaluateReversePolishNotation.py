from collections import deque
class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        if len(tokens) == 0:
            return 0
        tokens = deque(tokens)
        stack = []
        while tokens:
            nextChar = tokens.popleft()
            if nextChar == "+":
                tmp1 = stack.pop()
                tmp2 = stack.pop()
                stack.append(tmp2+tmp1)
            elif nextChar == "-":
                tmp1 = stack.pop()
                tmp2 = stack.pop()
                stack.append(tmp2-tmp1)
            elif nextChar == "*":
                tmp1 = stack.pop()
                tmp2 = stack.pop()
                stack.append(tmp2*tmp1)
            elif nextChar == "/":
                tmp1 = stack.pop()
                tmp2 = stack.pop()
                if tmp2*tmp1<0:
                    stack.append(-(abs(tmp2)/abs(tmp1)))
                else:
                    stack.append(tmp2/tmp1)
            else:
                stack.append(int(nextChar))
        return stack[0]

s = Solution()
print s.evalRPN(["2","1","+","3","*"])
print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
