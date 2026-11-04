class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(p):
            return (p[0]**2+p[1]**2)**0.5
        res = []
        heap = []
        for i in range(len(points)):
            points[i].insert(0,distance(points[i]))
            heapq.heappush(heap,points[i])
        for i in range(k):
            res.append(heapq.heappop(heap)[1:3])
        return res
        
