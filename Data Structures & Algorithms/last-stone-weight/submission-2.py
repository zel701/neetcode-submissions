class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        reverse = []
        for i in stones:
            reverse.append(-i)
        for i in reverse:
            heapq.heappush(heap,i)
        while len(heap)>1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if first == second:
                continue
            else:
                heapq.heappush(heap,first-second)
        if not heap:
            return 0
        return -heap[0]