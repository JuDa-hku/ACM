class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m*n-1
        return self.searchMatrixHelp(matrix, target, low, high)

    def indexToMatrix(self, matrix, index):
        m, n = len(matrix), len(matrix[0])
        row, col = index/n, index-n*(index/n)
        return matrix[row][col]
        
    def searchMatrixHelp(self, matrix, target, low, high):
#        print low, high
        if high<low:
            return False
        if low == high and self.indexToMatrix(matrix,low) == target:
            return True
        if low == high and self.indexToMatrix(matrix,low) != target:
            return False
        middle = (low+high)/2
        if self.indexToMatrix(matrix,middle) < target:
            return self.searchMatrixHelp(matrix, target, middle+1, high)
        if self.indexToMatrix(matrix,middle) == target:
            return True
        if self.indexToMatrix(matrix,middle) > target:
            return self.searchMatrixHelp(matrix, target, low, middle-1)

s = Solution()
matrix = [ [1],[3]
 ]
target = 1
print s.searchMatrix(matrix, target)