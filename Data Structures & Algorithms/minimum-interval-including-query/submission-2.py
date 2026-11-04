class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        import heapq
        intervals.sort(key=lambda x:x[0])
        original = queries.copy()
        queries.sort()
      
        result = {}
        heap = []
        output = []
        i = 0
        for q in queries:
            while i<len(intervals) and intervals[i][0]<=q:
                start,end = intervals[i][0],intervals[i][1]
                heapq.heappush(heap,(end-start+1,end))
                i+=1
            while heap and heap[0][1]<q:
                heapq.heappop(heap)
            if heap:
                result[q] = heap[0][0]
            else:
                result[q] = -1
        for i in original:
            output.append(result[i])
        return output

