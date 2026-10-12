class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_unvisited = []
        atlantic_unvisited = []
        h = len(heights)
        w = len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(h):
            pacific_unvisited.append((i, 0))
            atlantic_unvisited.append((i,w-1))
        for p in range(1, w):
            pacific_unvisited.append((0, p))
        for q in range(0,w-1):
            atlantic_unvisited.append((h-1,q))
        def bfs(unvisited):
            visited = set()
            for visit in unvisited:
                visited.add(visit)
            while unvisited:
                current = []
                for y, x in unvisited:
                    for j, k in directions:
                        if 0 <= y + j < h and 0 <= x + k < w and (y + j, x + k) not in visited and heights[y+j][x+k] >= heights[y][x]:
                            current.append((y + j, x + k))
                            visited.add((y + j, x + k))
                unvisited = current.copy()
            return visited
        pacific = bfs(pacific_unvisited)
        atlantic = bfs(atlantic_unvisited)
        both = []
        for i in range(h):
            for z in range(w):
                if (i,z) in pacific and (i,z) in atlantic:
                    both.append([i,z])
        return both