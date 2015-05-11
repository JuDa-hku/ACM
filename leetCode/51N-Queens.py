import copy
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        curr, state, sol = 0, [['.' for _ in xrange(n)] for _ in xrange(n)], []
        self.solveNQueensHelp(n, curr, state, sol)
        return sol

    def solveNQueensHelp(self, n, curr, state, sol):
        if curr == n:
            for row in xrange(n):
                for col in xrange(n):
                    if state[row][col] == '#':
                        state[row][col] ='.'
            res =[''.join(row) for row in state]
            sol.append(res)
        else:
            for i in xrange(n):
                if state[curr][i] == ".":
                    newState = self.updateState(n, curr,i, state)
                    self.solveNQueensHelp(n, curr+1, newState, sol)


    def updateState(self, n, row, col, state):
        newState = copy.deepcopy(state)
        newState[row][col] = 'Q'
        for i,j in zip([1,1,0,1],[1,-1,1,0]):
            currRow, currCol = row+i, col+j
            while currRow<n and currCol<n and currRow>=0 and currCol>=0:
                newState[currRow][currCol] = '#'
                currRow += i
                currCol += j
        return newState







import copy
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        curr, state, sol = 0, ['.'*n  for _ in xrange(n)], []
        self.solveNQueensHelp(n, curr, state, sol)
        return sol

    def solveNQueensHelp(self, n, curr, state, sol):
        if curr == n:
        #print res
            res = copy.deepcopy(state)
            sol.append(res)
        else:
            for i in xrange(n):
                if state[curr][i] == ".":
                    if self.checkState(n, curr,i, state):
                        state[curr] = state[curr][:i] + 'Q' +state[curr][i+1:]
                        self.solveNQueensHelp(n, curr+1, state, sol)
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