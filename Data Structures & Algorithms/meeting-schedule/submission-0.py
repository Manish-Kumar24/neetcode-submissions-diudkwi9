"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        start1, end1 = intervals[0].start, intervals[0].end
        for i in range(1, len(intervals)):
            start2, end2 = intervals[i].start, intervals[i].end
            if start2 < end1:
                return False
            start1, end1 = start2, end2
        return True