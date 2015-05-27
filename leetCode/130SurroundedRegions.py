class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        #transform o in the edge to be the '#' use dfs or bfs to make all o to be '#' then the left o is the o that should be x.
        if len(board) == 0:
            return
        m, n = len(board), len(board[0])
        checkedMatrix = [[False]*n for _ in xrange(m)]
        
        for i in xrange(m):
            for j in (0, n-1):
                if board[i][j] == 'O':
                    board[i][j] = '#'
        for i in (0, m-1):
            for j in xrange(n):
                if board[i][j] == 'O':
                    board[i][j] = '#'

        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == '#':
                    self.dfs(i, j, board, checkedMatrix)


        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'


        

    def dfs(self, row, col, board, checkedMatrix):
        m, n = len(board), len(board[0])
        if checkedMatrix[row][col]:
            return
        checkedMatrix[row][col] = True
        for i,j in zip((0,0,1,-1),(1,-1,0,0)):
            newRow, newCol = row+i, col+j

            if newRow>=m or newCol>=n:
                pass
            elif board[newRow][newCol] =='O':
                board[newRow][newCol] = '#'
                self.dfs(newRow, newCol, board, checkedMatrix)
            
                

s = Solution()
board = [['X', 'X','X', 'X'],
         ['X', 'O','O', 'X'],
         ['X', 'X','O', 'X'],
         ['X', 'O','O', 'X']
     ]
newBoard  = []
for i in board:
    newBoard.extend(i)
s.solve([newBoard])