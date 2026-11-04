class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort()
        current_end = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]>=current_end:
                current_end = intervals[i][1]
            else:
                count+=1
                current_end = min(current_end,intervals[i][1])
        return count