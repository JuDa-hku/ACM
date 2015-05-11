class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        n,m,res = len(matrix[0]),len(matrix),[]
        while n>0 and m>0:
            tmp = self.spiralOrderHelp(matrix, n, m)
            res.extend(tmp)
            n -= 2
            m -= 2
        return res


    def spiralOrderHelp(self, matrix, width, deep):
        n,m = len(matrix[0]),len(matrix)
        startWidth = (n-width)/2
        endWidth = startWidth+width-1
        startDeep = (m-deep)/2
        endDeep = startDeep+deep-1
        tmp = []
#        print startWidth,endWidth,startDeep,endDeep
        if startDeep == endDeep:
            for i in xrange(startWidth, endWidth+1, 1):
                tmp.append(matrix[startDeep][i])
            return tmp
        if startWidth == endWidth:
            for i in xrange(startDeep, endDeep+1, 1):
                tmp.append(matrix[i][startWidth])
            return tmp
        for i in xrange(startWidth, endWidth, 1):
            tmp.append(matrix[startDeep][i])
        for i in xrange(startDeep, endDeep, 1):
            tmp.append(matrix[i][endWidth])
        for i in xrange(endWidth, startWidth,-1):
            tmp.append(matrix[endDeep][i])
        for i in xrange(endDeep, startDeep,-1):
            tmp.append(matrix[i][startWidth])
        return tmp

s = Solution()
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

print s.spiralOrder(matrix)
print s.spiralOrderHelp(matrix,2,1)
matrix = [[5,9,7]]
matrix =[[7],[9],[6]]
#print s.spiralOrderHelp(matrix,3,1)
print s.spiralOrder(matrix)
        
        