class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 1
        empty = 0
        rotten = 2
        rottens = []
        h = len(grid)
        w = len(grid[0])
        count = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == rotten:
                    rottens.append((i,j))
                if grid[i][j] == fresh:
                    count+=1
        if not count:
            return 0
        visited = set()
        unvisited = rottens
        minutes = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        while unvisited:
            current = []
            for i,j in unvisited:
                if grid[i][j] == 1:
                    grid[i][j] = 2
                for x,y in directions:
                    if 0 <= j+x < w and 0 <= i+y < h and grid[i+y][j+x] == 1:
                        if (i+y,j+x) not in visited:
                            current.append((i+y,j+x))
                            visited.add((i+y,j+x))
                            count-=1
            minutes +=1
            unvisited = current
        if count == 0:
            return minutes-1
        return -1