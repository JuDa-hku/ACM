class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        if n <= 1:
            return
        C = set()
        for i in xrange(n):
            for j in xrange(n):
                if (i,j) not in C:
                    matrix[i][j], matrix[j][n-1-i] = matrix[j][n-1-i], matrix[i][j]
                    C.add((j,n-1-i))
        return

s = Solution()
matrix = [range(10) for _ in range(10)]
print matrix
s.rotate(matrix)
print matrix                