class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = defaultdict(int)
        for i in nums:
            numsDict[i]+=1
        heap = []
        for num,freq in numsDict.items():
            heapq.heappush(heap,(freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        sol = []
        for i in heap:
            sol.append(i[1])
        return sol