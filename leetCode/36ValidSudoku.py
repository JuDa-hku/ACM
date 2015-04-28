class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        newboard = self.transform(board)
        for i in range(len(board)):
            for j in range(len(board)):
                if not self.findOK(i,j, newboard):
                    return False
        return True


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
                if board[i][j] == '.':
                    continue
                if board[i][j] in includedSet:
                    return False
                else:
                    includedSet.add(board[i][j])
        includedSet = set()
        for num in board[row]:
            if num == '.':
                continue
            if num in includedSet:
                return False
            else:
                includedSet.add(num)
        includedSet = set()
        for i in range(len(board)):
            if board[i][col] == '.':
                continue
            if board[i][col] in includedSet:
                return False
            else:
                includedSet.add(board[i][col])
        return True


    def transform(self, board):
        newboard,m = [[0 for _ in range(9)] for _ in range(9) ], len(board)
        for pos in range(m*m):
            row, col = pos/m, pos%m
            if board[row][col] == '.':
                newboard[row][col] = '.'
            else:
                newboard[row][col] = int(board[row][col])
        return newboard


board1 = ["..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.", ".98...3..", "...8.3.2.", "........6", "...2759.."]

s = Solution()
print s.isValidSudoku(board1)

