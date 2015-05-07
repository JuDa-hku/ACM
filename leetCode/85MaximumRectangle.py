class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        matrix = self.transfrom(matrix)
        if len(matrix)<1:
            return 0
        start, height,width,maxRes = (0,0), len(matrix), len(matrix[0]), 20
        return self.maximalRectangleHelp(start, width, height, matrix, maxRes)


    def transfrom(self, matrix):
        newMatrix = []
        for tmp in matrix:
            tmp1 = [int(s) for s in tmp]
            newMatrix.append(tmp1)
        return newMatrix
        
    def maximalRectangleHelp(self, start, width, height, matrix, maxRes):
        if width*height<=maxRes:
            return maxRes
        tag = True
        for i in xrange(width):
            for j in xrange(height):
                if matrix[start[0]+j][start[1]+i] == 0:
                    tag = False
                    break
        if not tag:
            tmp1 = self.maximalRectangleHelp(start, width, j, matrix, maxRes)
            maxRes = max(tmp1, maxRes)
            tmp2 = self.maximalRectangleHelp(start, i, height, matrix, maxRes)
            maxRes = max(tmp2, maxRes)
            tmp3 = self.maximalRectangleHelp((start[0], start[1]+i+1), width-i-1, height, matrix, maxRes)
            maxRes = max(tmp3, maxRes)
            tmp4 = self.maximalRectangleHelp((start[0]+j+1, start[1]), width, height-j-1, matrix, maxRes)
            maxRes = max(tmp4, maxRes)
            return maxRes
        if tag:
            maxRes = max(width*height, maxRes)
        return maxRes

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        maxValue = 0
        n, m = len(matrix), len(matrix[0])
        leftMatrix, rightMatrix, heightMatrix = [0 for _ in xrange(m)], [m-1 for _ in xrange(m)], [0 for _ in xrange(m)]
        for i in xrange(n):
            cur_left, cur_right = 0, m-1
            for j in xrange(m):
                if matrix[i][j] == "0":
                    leftMatrix[j] = 0
                    cur_left = j+1
                else:
                    leftMatrix[j] = max(cur_left, leftMatrix[j])
            for j in xrange(m-1, -1, -1):
                if matrix[i][j] == "0":
                    rightMatrix[j] = m-1
                    cur_right = j-1
                else:
                    rightMatrix[j] = min(cur_right, rightMatrix[j])
            for j in xrange(m):
                if matrix[i][j] == "0":
                    heightMatrix[j] = 0
                else:
                    heightMatrix[j] = heightMatrix[j] + 1
                    maxValue = max((rightMatrix[j]-leftMatrix[j]+1)*heightMatrix[j], maxValue)
            print i, heightMatrix, leftMatrix, rightMatrix

        return maxValue

                
                

s = Solution()
matrix = ["01111","11111", "11111"]
matrix1 = ["0","0"]
matrix2 = ["0","1","1","0","1","1","1"]
matrix3 = ["000","000","111"]
matrix4 = ["1101","1101","1111"]
print s.maximalRectangle(matrix)
print s.maximalRectangle(matrix1)
print s.maximalRectangle(matrix2)
print s.maximalRectangle(matrix3)




matrix = ["1111111111111101001111111100111011111111","1111011011111111101101111101111111111111","0111101011111101101101101111111111111111","0101101011111111111101111111010110111111","1111111111110111110110010111111111111111","1111111110110101111111111101011111101111","0110110101110011111111111111110111110101","0111111111111100111111100110011011010101","1111011110111111111011011011110101101011","1111111110111111111101101101110111101111","1110110011111111111100111111111111111111","1011111110111101111001110111111111111111","0110111111111111101111110111011111011111","1111111111111111011111111111110111111011","1111100111111110101100111111111111101111","1111101111111110111111011111111111011111","1111101111111111111111011001111110011111","1111110111111111011111111111110111110111","1011111111111111010111110010111110111111","1111110011111111111110111111111111111011","1111111111111111110111011111011111011011","1100011011111111111111011111011111111111","1111101011111111111101100101110011111111","1110010111111111111011011110111101111101","1111111111111101101111111111101111111111","1111111011111101111011111111111110111111","1110011111111110111011111111110111110111","1111111111111100111111010111111111110111","1111111111111111111111000111111111011101","1111110111111111111111111101100111011011","1111011011111101101101111110111111101111","1111111111011111111111111111111111111111","1111111111111111111111111111111111111111","1100011111111110111111111111101111111011","1111101111111101111010111111111111111111","0111111111110011111111110101011011111111","1011011111101111111111101111111111110011","1010111111111111111111111111111110011111","0111101111011111111111111111110111111111","0111111011111111011101111011101111111111","0111111111110101111011111101011001111011","1111111111111011110111111101111111101110","1111101111111100111111111110111111001111","1101101111110101111101111111100111010100","0110111111100111110010111110111011011101"]
print s.maximalRectangle(matrix)                