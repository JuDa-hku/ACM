



import copy
class Solution:
    # @return a list of lists of string
    def totalNQueens(self, n):
        curr, state, count = 0, ['.'*n  for _ in xrange(n)], []
        self.solveNQueensHelp(n, curr, state, count)
        return len(count)

    def solveNQueensHelp(self, n, curr, state, count):
        if curr == n:
        #print res
            count.append(1)
        else:
            for i in xrange(n):
                if state[curr][i] == ".":
                    if self.checkState(n, curr,i, state):
                        state[curr] = state[curr][:i] + 'Q' +state[curr][i+1:]
                        self.solveNQueensHelp(n, curr+1, state, count)
                        state[curr] = state[curr][:i] + '.' +state[curr][i+1:]

    def checkState(self, n, row, col, state):
        for i,j in zip([-1,-1,-1],[0,-1,1]):
            currRow, currCol = row+i, col+j
            while currRow<n and currCol<n and currRow>=0 and currCol>=0:
                if state[currRow][currCol] == 'Q':
                    return False
                else:
                    currRow += i
                    currCol += j
        return True

s = Solution()
print s.solveNQueens(4)
print s.solveNQueens(8)
