class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        firstRow = False
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        firstRow = True
                        matrix[0][j] = 0
                    else:
                        matrix[0][j], matrix[i][0] = 0, 0
                        
        for i in xrange(1,m,1):
            if matrix[i][0] == 0:
                for j in xrange(n):
                    matrix[i][j] = 0

        for i in xrange(n):
            if matrix[0][i] == 0:
                for j in xrange(m):
                    matrix[j][i] = 0

        if firstRow:
            for j in xrange(n):
                matrix[0][j] = 0

        return

s = Solution()
matrix = [[0,1,1]]
s.setZeroes(matrix)
        
            
                    