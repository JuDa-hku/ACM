import copy 
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        newboard = self.transform(board)
        pos, res = 0, []
        self.solveSudokuHelp(pos, newboard,  res)
        for i in range(len(res)):
            tmpstr = [str(j) for j in res[i]]
            tmp = ''.join(tmpstr)
            board[i] = tmp
        return
        
    def solveSudokuHelp(self, pos, board, res):
        m = len(board)
        row, col = pos/m, pos%m
        if pos == m*m:
            tag, res[:] = True, copy.deepcopy(board)
            return
        if board[row][col] != '.':
            self.solveSudokuHelp(pos+1, board, res)
        else:
            posValid = self.findOK(row, col, board)
            if len(posValid) == 0:
                return
            for valid in posValid:
                board[row][col] = valid
                self.solveSudokuHelp(pos+1, board, res)
                board[row][col] = '.'
        return
        
    def findOK(self, row, col, board):
        if row%3 == 0:
            checkedRow = [row+1, row+2]
        if row%3 == 1:
            checkedRow = [row-1, row+1]
        if row%3 == 2:
            checkedRow = [row-1, row-2]
        if col%3 == 0:
            checkedCol = [col+1, col+2]
        if col%3 == 1:
            checkedCol = [col-1, col+1]
        if col%3 == 2:
            checkedCol = [col-1, col-2]
        includedSet = set()
        for i in checkedRow:
            for j in checkedCol:
                includedSet.add(board[i][j])
        for num in board[row]:
            includedSet.add(num);
        for i in range(len(board)):
            includedSet.add(board[i][col])
        res = []
        for i in range(1,10,1):
            if i not in includedSet:
                res.append(i)
        return res

    def transform(self, board):
        newboard,m = [[0 for _ in range(9)] for _ in range(9) ], len(board)
        for pos in range(m*m):
            row, col = pos/m, pos%m
            if board[row][col] == '.':
                newboard[row][col] = '.'
            else:
                newboard[row][col] = int(board[row][col])
        return newboard
        


        

board = [[5, 3, '.', '.', 7, '.', '.', '.', '.'],
         [6, '.', '.', 1, 9, 5, '.', '.', '.'],
         ['.', 9, 8, '.', '.', '.', '.', 6, '.'],
         [8, '.', '.', '.', 6, '.', '.', '.', 3],
         [4, '.', '.', 8, '.', 3, '.', '.', 1],
         [7, '.', '.', '.', 2, '.', '.', '.', 6],
         ['.', 6, '.', '.', '.', '.', 2, 8, '.'],
         ['.', '.', '.', 4, 1, 9, '.', '.', 5],
         ['.', '.', '.', '.', 8, '.', '.', 7,9]]

# board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
#          [6, 7, 2, 1, 9, 5, 3, 4, 8],
#          ['.', 9, 8, '.', '.', '.', '.', 6, '.'],
#          [8, 5, 9, 7, 6, 1, 4, 2, 3],
#          [4, '.', '.', 8, '.', 3, '.', '.', 1],
#          [7, '.', '.', '.', 2, '.', '.', '.', 6],
#          ['.', 6, '.', '.', '.', '.', 2, 8, '.'],
#          ['.', '.', '.', 4, 1, 9, '.', '.', 5],
#          ['.', '.', '.', '.', 8, '.', '.', 7,9]]


board1 = ["..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.", ".98...3..", "...8.3.2.", "........6", "...2759.."]

s = Solution()
print s.findOK(0, 3, board)
res, tag = [], False
s.solveSudokuHelp(0, board, res)
s.solveSudoku(board1)