"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        ends = []
        heapq.heapify(ends)
        intervals.sort(key = lambda x:x.start)
        for i in range(len(intervals)):
            heapq.heappush(ends,intervals[i].end)
            while ends and intervals[i].start>=ends[0]:
                heapq.heappop(ends)
            res = max(res,len(ends))
        return res
