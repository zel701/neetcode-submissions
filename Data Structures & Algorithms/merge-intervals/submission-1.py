class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i=0
        res = []
        while(i<len(intervals)):
            current = intervals[i]
            
            while i < len(intervals) - 1 and current[1] >= intervals[i+1][0]:
                current[1] = max(current[1],intervals[i+1][1])
                i+=1
                    
            res.append(current)
            i+=1
        return res

            