class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land = 2147483647
        water = -1
        treasure = 0
        treasures = []
        h = len(grid)
        w = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == treasure:
                    treasures.append((i,j))
        visited = set()
        unvisited = treasures
        distance = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        while unvisited:
            current = []
            for i,j in unvisited:
                if grid[i][j] == land:
                    grid[i][j] = distance
                for x,y in directions:
                    if 0 <= j+x < w and 0 <= i+y < h and grid[i+y][j+x] == land:
                        if (i+y,j+x) not in visited:
                            current.append((i+y,j+x))
                            visited.add((i+y,j+x))
            distance+=1
            unvisited = current
                    