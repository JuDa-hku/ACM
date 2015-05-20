class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        if len(board) == 0:
            return False
        if len(word) == 0:
            return True
        if type(board) == type(['d']):
            board = [''.join(string) for string in board]
#        print board
        n, m = len(board), len(board[0])
        boolMatrix = [[True]*m for _ in xrange(n)]
        for row in xrange(n):
            for col in xrange(m):
                if board[row][col] == word[0]:
#                    print row, col
                    boolMatrix[row][col] = False
                    if self.dfs(row, col, board, word[1:], boolMatrix):
                        return True
                    boolMatrix[row][col] = True
        return False

    def dfs(self, row, col, board, word, boolMatrix):
        n, m = len(board), len(board[0])
        if len(word) == 0:
            return True
        for i,j in zip([1,-1,0,0],[0,0,1,-1]):
            newRow, newCol = row+i, col+j
            if 0<=newRow<n and 0<=newCol<m:
#                print newRow, newCol,board, boolMatrix
                if board[newRow][newCol] == word[0] and boolMatrix[newRow][newCol]:
                    boolMatrix[newRow][newCol] = False
                    if self.dfs(newRow, newCol, board, word[1:], boolMatrix):
                        return True
                    boolMatrix[newRow][newCol] = True
        return False

s = Solution()
board = [
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
words = ["ABCCED", "SEE", "ABCB", ""]
for word in words:
    print s.exist(board, word)

print s.exist(["aa"], "aa")
print s.exist(["ab","cd"], "acdb")