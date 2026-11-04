class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        heap = []
        counts = Counter(tasks)
        for task,count in counts.items():
            heapq.heappush(heap,[-count,task])
        while len(heap)>0:
            current = []
            for i in range(n+1):
                if len(heap)==0 and not current:
                    return time
                elif heap:
                    time+=1
                    new = heapq.heappop(heap)
                    new[0]+=1
                    if new[0]<0:
                        current.append(new)
                else:
                    time+=1
            for i in current:
                heapq.heappush(heap,i)
        return time

        

