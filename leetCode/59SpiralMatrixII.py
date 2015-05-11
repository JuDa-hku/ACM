class Solution:
    # @param {integer} n
    # @return {integer[][]} 
    def generateMatrix(self, n):
        if n == 1:
            return [[1]]
        matrix = [[0 for _ in xrange(n)] for _ in xrange(n)]
        width,startValue = n,1
        while width>0 :
            startValue = self.generateMatrixHelp(matrix, width, startValue)
            width -= 2
        return matrix


    def generateMatrixHelp(self, matrix, width, startValue):
        n = len(matrix[0])
        startWidth = (n-width)/2
        endWidth = startWidth+width-1
#        print startWidth,endWidth,startDeep,endDeep
        if startWidth == endWidth:
                matrix[startWidth][startWidth] = startValue
                return startValue+1
        for i in xrange(startWidth, endWidth, 1):
            matrix[startWidth][i] = startValue
            startValue += 1
        for i in xrange(startWidth, endWidth, 1):
            matrix[i][endWidth] = startValue
            startValue += 1
        for i in xrange(endWidth, startWidth,-1):
            matrix[endWidth][i] = startValue
            startValue += 1
        for i in xrange(endWidth, startWidth,-1):
            matrix[i][startWidth] = startValue
            startValue += 1
        return startValue

s = Solution()
print s.generateMatrix(2)
        
        