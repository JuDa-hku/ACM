class Solution:

    def dfs(self,x, y, grid):
        grid[x][y] = 0
        for i,j in zip([0,0,-1,1], [1,-1,0,0]):
            row = x+i
            col = y+j
            inRow = row<len(grid) and row>=0
            inCol = col<len(grid[0]) and col>=0
            if inRow and inCol:
                if grid[row][col] == '1':
                    grid[row][col] = '0'
                    self.dfs(row, col, grid)

    
    def numIslands(self,grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(i, j, grid)
        return count

grid = [['1','1','0'],
        ['1','1','0'],
        ['1','1','0'],
        ['0','0','0']]
a = Solution()
print grid
print a.numIslands(grid)

# grid = [[1,1,0,0,0],
#         [1,1,0,0,0],
#         [0,0,1,0,0],
#         [0,0,0,1,1]]
# print countIsland(grid)