class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def findNearby(matrix,x,y):
            count = 0 
            if matrix[y][x] == 1:
                count+=1
                matrix[y][x] = "0.5"
                if x-1>=0:
                    count += findNearby(matrix,x-1,y)
                if x+1<len(matrix[0]):
                    count += findNearby(matrix,x+1,y)
                if y-1>=0:
                    count += findNearby(matrix,x,y-1)
                if y+1<len(matrix):
                    count += findNearby(matrix,x,y+1)
            return count
        Max = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    Max = max(findNearby(grid,j,i),Max)
        return Max