class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def findNearby(matrix,x,y):
            if matrix[y][x] == "1":
                matrix[y][x] = "0.5"
                if x-1>=0:
                    findNearby(matrix,x-1,y)
                if x+1<len(matrix[0]):
                    findNearby(matrix,x+1,y)
                if y-1>=0:
                    findNearby(matrix,x,y-1)
                if y+1<len(matrix):
                    findNearby(matrix,x,y+1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count+=1
                    findNearby(grid,j,i)
        return count
                