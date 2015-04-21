class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer

    
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        ##d denotes how many hp do we need to continue our search
        ##start from the right bottom
        d = [0 for i in xrange(n)]
        d[n-1] = max(1,1-dungeon[m-1][n-1])
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if row+1 == m and col+1==n:
                    continue
                if row+1 == m:
                    dRowPlus = float('inf')
                else:
                    dRowPlus = d[col]
                if col+1 == n:
                    dColPlus = float('inf')
                else:
                    dColPlus = d[col+1]
                d[col] = max(min(dRowPlus, dColPlus)-dungeon[row][col],1)
        return d[0]
                
                

s = Solution()
dungeon = [[-2,-3,3], [-5,-10,1], [10,30,-5]]
dungeon = [[1,-3,3], [0,-2,0], [-3,-3,-3]]
print s.calculateMinimumHP(dungeon)
                
                    
        
        